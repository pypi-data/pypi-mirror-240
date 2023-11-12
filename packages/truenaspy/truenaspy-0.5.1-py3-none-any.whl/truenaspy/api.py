"""TrueNAS API."""
from __future__ import annotations

from datetime import datetime, timedelta
from logging import getLogger
from typing import Any, Self

from aiohttp import ClientSession

from .auth import Auth
from .collects import (
    Alerts,
    Boot,
    Charts,
    CloudSync,
    Datasets,
    Disk,
    Interfaces,
    Jail,
    Job,
    Pool,
    Replication,
    Rsync,
    Service,
    Smart,
    Snapshottask,
    System,
    Update,
    VirtualMachine,
)
from .exceptions import TruenasError
from .helper import (
    as_local,
    b2gib,
    search_attrs,
    systemstats_process,
    utc_from_timestamp,
)
from .subscription import Events, Subscriptions

_LOGGER = getLogger(__name__)


class TruenasClient(object):
    """Handle all communication with TrueNAS."""

    def __init__(
        self,
        host: str,
        token: str,
        session: ClientSession | None = None,
        use_ssl: bool = False,
        verify_ssl: bool = True,
        scan_intervall: int = 60,
        timeout: int = 300,
    ) -> None:
        """Initialize the TrueNAS API."""
        self._access = Auth(host, token, use_ssl, verify_ssl, timeout, session)
        self._is_scale: bool = False
        self._is_virtual: bool = False
        self._sub = Subscriptions(
            (self.async_update_all, self.async_is_alive), scan_intervall
        )
        self._systemstats_errored: list[str] = []
        self.query = self._access.async_request
        self.alerts: list[dict[str, Any]] = []
        self.charts: list[dict[str, Any]] = []
        self.cloudsync: list[dict[str, Any]] = []
        self.data: dict[str, Any] = {}
        self.datasets: list[dict[str, Any]] = []
        self.disks: list[dict[str, Any]] = []
        self.interfaces: list[dict[str, Any]] = []
        self.jails: list[dict[str, Any]] = []
        self.pools: list[dict[str, Any]] = []
        self.replications: list[dict[str, Any]] = []
        self.rsynctasks: list[dict[str, Any]] = []
        self.services: list[dict[str, Any]] = []
        self.smarts: list[dict[str, Any]] = []
        self.snapshots: list[dict[str, Any]] = []
        self.stats: dict[str, Any] = {}
        self.system: dict[str, Any] = {}
        self.virtualmachines: list[dict[str, Any]] = []

    async def async_get_system(self) -> dict[str, Any]:
        """Get system info from TrueNAS."""
        response = await self.query(path="system/info")
        self.system = search_attrs(System, response)

        response = await self.query(path="system/version_short")
        self.system.update({"short_version": response})

        response = await self.query(path="/update/get_trains")
        self.system.update({"current_train": response.get("current")})

        # update_available
        response = await self.query(path="update/check_available", method="post")
        update = search_attrs(Update, response)
        self.system.update(update)

        # update_version
        if not update["update_available"]:
            self.system.update({"update_version": self.system["version"]})

        if (update_jobid := self.system.get("update_jobid")) is not None:
            response = await self.query(
                path="core/get_jobs", params={"id": update_jobid}
            )
            jobs = search_attrs(Job, response)
            for job in jobs:
                if (
                    job.get("update_state") != "RUNNING"
                    or not update["update_available"]
                ):
                    self.system.update(
                        {
                            "update_progress": 0,
                            "update_jobid": 0,
                            "update_state": "unknown",
                        }
                    )

        response = await self.query(path="/system/is_freenas")
        self._is_scale = response is False
        self._is_virtual = self.system["system_manufacturer"] in [
            "QEMU",
            "VMware, Inc.",
        ] or self.system["system_product"] in ["VirtualBox"]

        if (uptime := self.system["uptime_seconds"]) > 0:
            now = datetime.now().replace(microsecond=0)
            uptime_tm = datetime.timestamp(now - timedelta(seconds=int(uptime)))
            self.system.update(
                {
                    "uptimeEpoch": str(
                        as_local(utc_from_timestamp(uptime_tm)).isoformat()
                    )
                }
            )

        query = [
            {"name": "load"},
            {"name": "cpu"},
            {"name": "arcsize"},
            {"name": "arcratio"},
            {"name": "memory"},
        ]

        if not self._is_virtual:
            query.append({"name": "cputemp"})

        stats: list[dict[str, Any]] = await self.async_get_stats(query)
        for item in stats:
            # CPU temperature
            if item.get("name") == "cputemp" and "aggregations" in item:
                self.system["cpu_temperature"] = round(
                    max(list(filter(None, item["aggregations"]["mean"]))), 1
                )

            # CPU load
            if item.get("name") == "load":
                tmp_arr = ["load_shortterm", "load_midterm", "load_longterm"]
                systemstats_process(self.system, tmp_arr, item, "")

            # CPU usage
            if item.get("name") == "cpu":
                tmp_arr = ["interrupt", "system", "user", "nice", "idle"]
                systemstats_process(self.system, tmp_arr, item, "cpu")
                self.system["cpu_usage"] = round(
                    self.system["cpu_system"] + self.system["cpu_user"], 2
                )

            # arcratio
            if item.get("name") == "memory":
                tmp_arr = [
                    "memory-used_value",
                    "memory-free_value",
                    "memory-cached_value",
                    "memory-buffered_value",
                ]
                systemstats_process(self.system, tmp_arr, item, "memory")
                self.system["memory_total_value"] = round(
                    self.system["memory-used_value"]
                    + self.system["memory-free_value"]
                    + self.system["cache_size-arc_value"],
                    2,
                )
                if (total_value := self.system["memory_total_value"]) > 0:
                    self.system["memory_usage_percent"] = round(
                        100
                        * (float(total_value) - float(self.system["memory-free_value"]))
                        / float(total_value),
                        0,
                    )

            # arcsize
            if item.get("name") == "arcsize":
                tmp_arr = ["cache_size-arc_value", "cache_size-L2_value"]
                systemstats_process(self.system, tmp_arr, item, "memory")

            # arcratio
            if item.get("name") == "arcratio":
                tmp_arr = ["cache_ratio-arc_value", "cache_ratio-L2_value"]
                systemstats_process(self.system, tmp_arr, item, "")

        self.data["systeminfos"] = self.system
        self._sub.notify(Events.SYSTEM.value)
        return self.system

    async def async_get_interfaces(self) -> list[dict[str, Any]]:
        """Get interface info from TrueNAS."""
        response = await self.query(path="interface")
        self.interfaces = search_attrs(Interfaces, response)
        query = [{"name": "interface", "identifier": uid} for uid in self.interfaces]
        stats = await self.async_get_stats(query)
        for item in stats:
            # Interface
            if (
                item.get("name") == "interface"
                and (identifier := item["identifier"]) in self.interfaces
            ):
                # 12->13 API change
                item["legend"] = [
                    legend.replace("if_octets_", "") for legend in item["legend"]
                ]

                systemstats_process(
                    self.interfaces[identifier], ["rx", "tx"], item, "rx-tx"
                )

        self.data["interfaces"] = self.interfaces
        self._sub.notify(Events.INTERFACES.value)
        return self.interfaces

    async def async_get_stats(self, items: list[dict[str, Any]]) -> Any:
        """Get statistics."""
        query: dict[str, Any] = {
            "graphs": items,
            "reporting_query": {
                "start": "now-90s",
                "end": "now-30s",
                "aggregate": True,
            },
        }

        for param in query["graphs"]:
            if param["name"] in self._systemstats_errored:
                query["graphs"].remove(param)

        stats = []
        try:
            stats = await self._access.async_request(
                "reporting/get_data", method="post", json=query
            )

            if "error" in stats:
                for param in query["graphs"]:
                    await self._access.async_request(
                        "reporting/get_data",
                        method="post",
                        json={
                            "graphs": [param],
                            "reporting_query": {
                                "start": "now-90s",
                                "end": "now-30s",
                                "aggregate": True,
                            },
                        },
                    )
                    if "error" in stats:
                        self._systemstats_errored.append(param["name"])

                _LOGGER.warning(
                    "Fetching following graphs failed, check your NAS: %s",
                    self._systemstats_errored,
                )
                await self.async_get_stats(items)
        except TruenasError as error:
            # ERROR FIX: Cobia NAS-123862
            if self.system.get("current_train") not in [
                "TrueNAS-SCALE-Cobia"
            ] and self.system.get("short_version") not in ["23.10.0.1"]:
                _LOGGER.error(error)

        return stats

    async def async_get_services(self) -> list[dict[str, Any]]:
        """Get service info from TrueNAS."""
        response = await self.query(path="service")
        self.services = search_attrs(Service, response)
        self.data["services"] = self.services
        self._sub.notify(Events.SERVICES.value)
        return self.services

    async def async_get_pools(self) -> list[dict[str, Any]]:
        """Get pools from TrueNAS."""
        response = await self.query(path="pool")
        self.pools = search_attrs(Pool, response)
        response = await self.query(path="boot/get_state")
        boot = search_attrs(Boot, response)
        self.pools.append(boot)

        # Process pools
        dataset_available = {}
        dataset_total = {}
        for dataset in self.datasets:
            if mountpoint := dataset.get("mountpoint"):
                available = dataset.get("available", 0)
                dataset_available[mountpoint] = b2gib(available)
                dataset_total[mountpoint] = b2gib(available + dataset.get("used", 0))

        for pool in self.pools:
            if value := dataset_available.get(pool["path"]):
                pool.update({"available_gib": value})

            if value := dataset_total.get(pool["path"]):
                pool.update({"total_gib": value})

            if pool["name"] in ["boot-pool", "freenas-boot"]:
                pool.update({"available_gib": b2gib(pool["root_dataset_available"])})
                pool.update(
                    {
                        "total_gib": b2gib(
                            pool["root_dataset_available"] + pool["root_dataset_used"]
                        )
                    }
                )
                # self.pools[uid].pop("root_dataset")

        self.data["pools"] = self.pools
        self._sub.notify(Events.POOLS.value)
        return self.pools

    async def async_get_datasets(self) -> list[dict[str, Any]]:
        """Get datasets from TrueNAS."""
        # response = await self.query(path="pool/dataset/details")
        response = await self.query(path="pool/dataset")
        self.datasets = search_attrs(Datasets, response)
        self.data["datasets"] = self.datasets
        self._sub.notify(Events.DATASETS.value)
        return self.datasets

    async def async_get_disks(self) -> list[dict[str, Any]]:
        """Get disks from TrueNAS."""
        response = await self.query(path="disk")
        self.disks = search_attrs(Disk, response)
        # Get disk temperatures
        temperatures = await self._access.async_request(
            "disk/temperatures", method="post", json={"names": []}
        )
        for disk in self.disks:
            disk.update({"temperature": temperatures.get(disk["name"], 0)})
        self.data["disks"] = self.disks
        self._sub.notify(Events.DISKS.value)
        return self.disks

    async def async_get_jails(self) -> list[dict[str, Any]] | None:
        """Get jails from TrueNAS."""
        if not self._is_scale:
            response = await self.query(path="jail")
            self.jails = search_attrs(Jail, response)
            self.data["jails"] = self.jails
            self._sub.notify(Events.JAILS.value)
        return self.jails

    async def async_get_virtualmachines(self) -> list[dict[str, Any]]:
        """Get VMs from TrueNAS."""
        response = await self.query(path="vm")
        self.virtualmachines = search_attrs(VirtualMachine, response)
        self.data["virtualmachines"] = self.virtualmachines
        self._sub.notify(Events.VMS.value)
        return self.virtualmachines

    async def async_get_cloudsync(self) -> list[dict[str, Any]]:
        """Get cloudsync from TrueNAS."""
        response = await self.query(path="cloudsync")
        self.cloudsync = search_attrs(CloudSync, response)
        self.data["cloudsync"] = self.cloudsync
        self._sub.notify(Events.CLOUD.value)
        return self.cloudsync

    async def async_get_replications(self) -> list[dict[str, Any]]:
        """Get replication from TrueNAS."""
        response = await self.query(path="replication")
        self.replications = search_attrs(Replication, response)
        self.data["replications"] = self.replications
        self._sub.notify(Events.REPLS.value)
        return self.replications

    async def async_get_snapshottasks(self) -> list[dict[str, Any]]:
        """Get replication from TrueNAS."""
        response = await self.query(path="pool/snapshottask")
        self.snapshots = search_attrs(Snapshottask, response)
        self.data["snapshots"] = self.snapshots
        self._sub.notify(Events.SNAPS.value)
        return self.snapshots

    async def async_get_charts(self) -> list[dict[str, Any]]:
        """Get Charts from TrueNAS."""
        response = await self.query(path="chart/release")
        self.charts = search_attrs(Charts, response)
        self.data["charts"] = self.charts
        self._sub.notify(Events.CHARTS.value)
        return self.charts

    async def async_get_smartdisks(self) -> list[dict[str, Any]]:
        """Get smartdisk from TrueNAS."""
        response = await self.query(path="/smart/test/results", params={"offset": 1})
        self.smarts = search_attrs(Smart, response)
        self.data["smarts"] = self.smarts
        self._sub.notify(Events.SMARTS.value)
        return self.smarts

    async def async_get_alerts(self) -> list[dict[str, Any]]:
        """Get smartdisk from TrueNAS."""
        response = await self.query(path="/alert/list")
        self.alerts = search_attrs(Alerts, response)
        self.data["alerts"] = self.alerts
        self._sub.notify(Events.ALERTS.value)
        return self.alerts

    async def async_get_rsynctasks(self) -> list[dict[str, Any]]:
        """Get smartdisk from TrueNAS."""
        response = await self.query(path="rsynctask")
        self.rsynctasks = search_attrs(Rsync, response)
        self.data["rsynctasks"] = self.rsynctasks
        self._sub.notify(Events.RSYNC.value)
        return self.rsynctasks

    def subscribe(self, _callback: str, *args: Any) -> None:
        """Subscribe event."""
        self._sub.subscribe(_callback, *args)

    def unsubscribe(self, _callback: str, *args: Any) -> None:
        """Unsubscribe event."""
        self._sub.subscribe(_callback, *args)

    async def async_update_all(self) -> dict[str, Any]:
        """Update all datas."""
        for event in Events:
            try:
                if event.name != "ALL":
                    fnc = getattr(self, f"async_get_{event.value}")
                    await fnc()
            except TruenasError as error:
                _LOGGER.error(error)
        self._sub.notify(Events.ALL.value)
        return self.data

    async def async_is_alive(self) -> bool:
        """Check connection."""
        result = await self._access.async_request("core/ping")
        return "pong" in result

    async def async_close(self) -> None:
        """Close open client session."""
        await self._access.async_close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The LaMetricCloud object.
        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.async_close()
