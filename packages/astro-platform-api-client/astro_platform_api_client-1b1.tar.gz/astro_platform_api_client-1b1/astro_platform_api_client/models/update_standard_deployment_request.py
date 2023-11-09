from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_standard_deployment_request_executor import UpdateStandardDeploymentRequestExecutor
from ..models.update_standard_deployment_request_scheduler_size import UpdateStandardDeploymentRequestSchedulerSize
from ..models.update_standard_deployment_request_type import UpdateStandardDeploymentRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_environment_variable_request import DeploymentEnvironmentVariableRequest
    from ..models.worker_queue_request import WorkerQueueRequest


T = TypeVar("T", bound="UpdateStandardDeploymentRequest")


@_attrs_define
class UpdateStandardDeploymentRequest:
    """
    Attributes:
        default_task_pod_cpu (str): The default CPU resource usage for a worker Pod when running the Kubernetes executor
            or KubernetesPodOperator. Units are in number of CPU cores. Example: 0.5.
        default_task_pod_memory (str): The default memory resource usage for a worker Pod when running the Kubernetes
            executor or KubernetesPodOperator. Units are in `Gi`. This value must always be twice the value of
            `DefaultTaskPodCpu`. Example: 1.
        environment_variables (List['DeploymentEnvironmentVariableRequest']): List of environment variables to add to
            the Deployment.
        executor (UpdateStandardDeploymentRequestExecutor): The executor Deployment's executor. Example: CELERY.
        is_cicd_enforced (bool): Whether the Deployment requires that all deploys are made through CI/CD. Example: True.
        is_dag_deploy_enabled (bool): Whether the Deployment has DAG deploys enabled. Example: True.
        is_high_availability (bool): Whether the Deployment is configured for high availability. If `true`, multiple
            scheduler pods will be online. Example: True.
        name (str): The Deployment's name. Example: My deployment.
        resource_quota_cpu (str): The CPU quota for worker Pods when running the Kubernetes executor or
            KubernetesPodOperator. If current CPU usage across all workers exceeds the quota, no new worker Pods can be
            scheduled. Units are in number of CPU cores. Example: 160.
        resource_quota_memory (str): The memory quota for worker Pods when running the Kubernetes executor or
            KubernetesPodOperator. If current memory usage across all workers exceeds the quota, no new worker Pods can be
            scheduled. Units are in `Gi`. This value must always be twice the value of `ResourceQuotaCpu`. Example: 320Gi.
        scheduler_size (UpdateStandardDeploymentRequestSchedulerSize): The size of the scheduler pod. Example: MEDIUM.
        type (UpdateStandardDeploymentRequestType): The type of the Deployment. Example: DEDICATED.
        workspace_id (str): The ID of the Workspace to which the Deployment belongs. Example: clmh7vdf4000008lhhlnk9t6o.
        contact_emails (Union[Unset, List[str]]): A list of contact emails for the Deployment. Example:
            ['user1@company.com'].
        description (Union[Unset, str]): The Deployment's description. Example: My deployment description.
        worker_queues (Union[Unset, List['WorkerQueueRequest']]): A list of the Deployment's worker queues. Applies only
            when `Executor` is `CELERY`. All Deployments need at least 1 worker queue called `default`.
        workload_identity (Union[Unset, str]): The Deployment's workload identity. Example:
            arn:aws:iam::123456789:role/AirflowS3Logs-clmk2qqia000008mhff3ndjr0.
    """

    default_task_pod_cpu: str
    default_task_pod_memory: str
    environment_variables: List["DeploymentEnvironmentVariableRequest"]
    executor: UpdateStandardDeploymentRequestExecutor
    is_cicd_enforced: bool
    is_dag_deploy_enabled: bool
    is_high_availability: bool
    name: str
    resource_quota_cpu: str
    resource_quota_memory: str
    scheduler_size: UpdateStandardDeploymentRequestSchedulerSize
    type: UpdateStandardDeploymentRequestType
    workspace_id: str
    contact_emails: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    worker_queues: Union[Unset, List["WorkerQueueRequest"]] = UNSET
    workload_identity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_task_pod_cpu = self.default_task_pod_cpu
        default_task_pod_memory = self.default_task_pod_memory
        environment_variables = []
        for environment_variables_item_data in self.environment_variables:
            environment_variables_item = environment_variables_item_data.to_dict()

            environment_variables.append(environment_variables_item)

        executor = self.executor.value

        is_cicd_enforced = self.is_cicd_enforced
        is_dag_deploy_enabled = self.is_dag_deploy_enabled
        is_high_availability = self.is_high_availability
        name = self.name
        resource_quota_cpu = self.resource_quota_cpu
        resource_quota_memory = self.resource_quota_memory
        scheduler_size = self.scheduler_size.value

        type = self.type.value

        workspace_id = self.workspace_id
        contact_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contact_emails, Unset):
            contact_emails = self.contact_emails

        description = self.description
        worker_queues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.worker_queues, Unset):
            worker_queues = []
            for worker_queues_item_data in self.worker_queues:
                worker_queues_item = worker_queues_item_data.to_dict()

                worker_queues.append(worker_queues_item)

        workload_identity = self.workload_identity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultTaskPodCpu": default_task_pod_cpu,
                "defaultTaskPodMemory": default_task_pod_memory,
                "environmentVariables": environment_variables,
                "executor": executor,
                "isCicdEnforced": is_cicd_enforced,
                "isDagDeployEnabled": is_dag_deploy_enabled,
                "isHighAvailability": is_high_availability,
                "name": name,
                "resourceQuotaCpu": resource_quota_cpu,
                "resourceQuotaMemory": resource_quota_memory,
                "schedulerSize": scheduler_size,
                "type": type,
                "workspaceId": workspace_id,
            }
        )
        if contact_emails is not UNSET:
            field_dict["contactEmails"] = contact_emails
        if description is not UNSET:
            field_dict["description"] = description
        if worker_queues is not UNSET:
            field_dict["workerQueues"] = worker_queues
        if workload_identity is not UNSET:
            field_dict["workloadIdentity"] = workload_identity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_environment_variable_request import DeploymentEnvironmentVariableRequest
        from ..models.worker_queue_request import WorkerQueueRequest

        d = src_dict.copy()
        default_task_pod_cpu = d.pop("defaultTaskPodCpu")

        default_task_pod_memory = d.pop("defaultTaskPodMemory")

        environment_variables = []
        _environment_variables = d.pop("environmentVariables")
        for environment_variables_item_data in _environment_variables:
            environment_variables_item = DeploymentEnvironmentVariableRequest.from_dict(environment_variables_item_data)

            environment_variables.append(environment_variables_item)

        executor = UpdateStandardDeploymentRequestExecutor(d.pop("executor"))

        is_cicd_enforced = d.pop("isCicdEnforced")

        is_dag_deploy_enabled = d.pop("isDagDeployEnabled")

        is_high_availability = d.pop("isHighAvailability")

        name = d.pop("name")

        resource_quota_cpu = d.pop("resourceQuotaCpu")

        resource_quota_memory = d.pop("resourceQuotaMemory")

        scheduler_size = UpdateStandardDeploymentRequestSchedulerSize(d.pop("schedulerSize"))

        type = UpdateStandardDeploymentRequestType(d.pop("type"))

        workspace_id = d.pop("workspaceId")

        contact_emails = cast(List[str], d.pop("contactEmails", UNSET))

        description = d.pop("description", UNSET)

        worker_queues = []
        _worker_queues = d.pop("workerQueues", UNSET)
        for worker_queues_item_data in _worker_queues or []:
            worker_queues_item = WorkerQueueRequest.from_dict(worker_queues_item_data)

            worker_queues.append(worker_queues_item)

        workload_identity = d.pop("workloadIdentity", UNSET)

        update_standard_deployment_request = cls(
            default_task_pod_cpu=default_task_pod_cpu,
            default_task_pod_memory=default_task_pod_memory,
            environment_variables=environment_variables,
            executor=executor,
            is_cicd_enforced=is_cicd_enforced,
            is_dag_deploy_enabled=is_dag_deploy_enabled,
            is_high_availability=is_high_availability,
            name=name,
            resource_quota_cpu=resource_quota_cpu,
            resource_quota_memory=resource_quota_memory,
            scheduler_size=scheduler_size,
            type=type,
            workspace_id=workspace_id,
            contact_emails=contact_emails,
            description=description,
            worker_queues=worker_queues,
            workload_identity=workload_identity,
        )

        update_standard_deployment_request.additional_properties = d
        return update_standard_deployment_request

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
