from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_quota_options import ResourceQuotaOptions
    from ..models.runtime_release import RuntimeRelease
    from ..models.scheduler_machine import SchedulerMachine
    from ..models.worker_machine import WorkerMachine
    from ..models.worker_queue_options import WorkerQueueOptions
    from ..models.workload_identity_option import WorkloadIdentityOption


T = TypeVar("T", bound="DeploymentOptions")


@_attrs_define
class DeploymentOptions:
    """
    Attributes:
        executors (List[str]): The available executors.
        resource_quotas (ResourceQuotaOptions):
        runtime_releases (List['RuntimeRelease']): The available Astro Runtime versions.
        scheduler_machines (List['SchedulerMachine']): The available scheduler sizes.
        worker_machines (List['WorkerMachine']): The available worker machine types.
        worker_queues (WorkerQueueOptions):
        workload_identity_options (Union[Unset, List['WorkloadIdentityOption']]): The available workload identity
            options.
    """

    executors: List[str]
    resource_quotas: "ResourceQuotaOptions"
    runtime_releases: List["RuntimeRelease"]
    scheduler_machines: List["SchedulerMachine"]
    worker_machines: List["WorkerMachine"]
    worker_queues: "WorkerQueueOptions"
    workload_identity_options: Union[Unset, List["WorkloadIdentityOption"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        executors = self.executors

        resource_quotas = self.resource_quotas.to_dict()

        runtime_releases = []
        for runtime_releases_item_data in self.runtime_releases:
            runtime_releases_item = runtime_releases_item_data.to_dict()

            runtime_releases.append(runtime_releases_item)

        scheduler_machines = []
        for scheduler_machines_item_data in self.scheduler_machines:
            scheduler_machines_item = scheduler_machines_item_data.to_dict()

            scheduler_machines.append(scheduler_machines_item)

        worker_machines = []
        for worker_machines_item_data in self.worker_machines:
            worker_machines_item = worker_machines_item_data.to_dict()

            worker_machines.append(worker_machines_item)

        worker_queues = self.worker_queues.to_dict()

        workload_identity_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workload_identity_options, Unset):
            workload_identity_options = []
            for workload_identity_options_item_data in self.workload_identity_options:
                workload_identity_options_item = workload_identity_options_item_data.to_dict()

                workload_identity_options.append(workload_identity_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executors": executors,
                "resourceQuotas": resource_quotas,
                "runtimeReleases": runtime_releases,
                "schedulerMachines": scheduler_machines,
                "workerMachines": worker_machines,
                "workerQueues": worker_queues,
            }
        )
        if workload_identity_options is not UNSET:
            field_dict["workloadIdentityOptions"] = workload_identity_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource_quota_options import ResourceQuotaOptions
        from ..models.runtime_release import RuntimeRelease
        from ..models.scheduler_machine import SchedulerMachine
        from ..models.worker_machine import WorkerMachine
        from ..models.worker_queue_options import WorkerQueueOptions
        from ..models.workload_identity_option import WorkloadIdentityOption

        d = src_dict.copy()
        executors = cast(List[str], d.pop("executors"))

        resource_quotas = ResourceQuotaOptions.from_dict(d.pop("resourceQuotas"))

        runtime_releases = []
        _runtime_releases = d.pop("runtimeReleases")
        for runtime_releases_item_data in _runtime_releases:
            runtime_releases_item = RuntimeRelease.from_dict(runtime_releases_item_data)

            runtime_releases.append(runtime_releases_item)

        scheduler_machines = []
        _scheduler_machines = d.pop("schedulerMachines")
        for scheduler_machines_item_data in _scheduler_machines:
            scheduler_machines_item = SchedulerMachine.from_dict(scheduler_machines_item_data)

            scheduler_machines.append(scheduler_machines_item)

        worker_machines = []
        _worker_machines = d.pop("workerMachines")
        for worker_machines_item_data in _worker_machines:
            worker_machines_item = WorkerMachine.from_dict(worker_machines_item_data)

            worker_machines.append(worker_machines_item)

        worker_queues = WorkerQueueOptions.from_dict(d.pop("workerQueues"))

        workload_identity_options = []
        _workload_identity_options = d.pop("workloadIdentityOptions", UNSET)
        for workload_identity_options_item_data in _workload_identity_options or []:
            workload_identity_options_item = WorkloadIdentityOption.from_dict(workload_identity_options_item_data)

            workload_identity_options.append(workload_identity_options_item)

        deployment_options = cls(
            executors=executors,
            resource_quotas=resource_quotas,
            runtime_releases=runtime_releases,
            scheduler_machines=scheduler_machines,
            worker_machines=worker_machines,
            worker_queues=worker_queues,
            workload_identity_options=workload_identity_options,
        )

        deployment_options.additional_properties = d
        return deployment_options

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
