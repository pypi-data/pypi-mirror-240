from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_hybrid_deployment_request_executor import CreateHybridDeploymentRequestExecutor
from ..models.create_hybrid_deployment_request_type import CreateHybridDeploymentRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_instance_spec_request import DeploymentInstanceSpecRequest
    from ..models.hybrid_worker_queue_request import HybridWorkerQueueRequest


T = TypeVar("T", bound="CreateHybridDeploymentRequest")


@_attrs_define
class CreateHybridDeploymentRequest:
    """
    Attributes:
        astro_runtime_version (str): Deployment's Astro Runtime version. Example: 9.1.0.
        cluster_id (str): The ID of the cluster where the Deployment will be created. Example:
            clmh9grqp000108mg4r2l5ok4.
        executor (CreateHybridDeploymentRequestExecutor): The Deployment's executor type. Example: CELERY.
        is_cicd_enforced (bool): Whether the Deployment requires that all deploys are made through CI/CD. Example: True.
        is_dag_deploy_enabled (bool): Whether the Deployment has DAG deploys enabled. Example: True.
        name (str): The Deployment's name. Example: My deployment.
        scheduler (DeploymentInstanceSpecRequest):
        type (CreateHybridDeploymentRequestType): The type of the Deployment. Example: DEDICATED.
        workspace_id (str): The ID of the workspace to which the Deployment belongs. Example: clmh8ol3x000008jo656y4285.
        description (Union[Unset, str]): The Deployment's description. Example: My deployment description.
        task_pod_node_pool_id (Union[Unset, str]): The node pool ID for the task pods. For `KUBERNETES` executor only.
            Example: clmh9hbjb000008m9eutqg68h.
        worker_queues (Union[Unset, List['HybridWorkerQueueRequest']]): The list of worker queues configured for the
            Deployment. Applies only when `Executor` is `CELERY`. At least 1 worker queue is needed. All Deployments need at
            least 1 worker queue called `default`.
    """

    astro_runtime_version: str
    cluster_id: str
    executor: CreateHybridDeploymentRequestExecutor
    is_cicd_enforced: bool
    is_dag_deploy_enabled: bool
    name: str
    scheduler: "DeploymentInstanceSpecRequest"
    type: CreateHybridDeploymentRequestType
    workspace_id: str
    description: Union[Unset, str] = UNSET
    task_pod_node_pool_id: Union[Unset, str] = UNSET
    worker_queues: Union[Unset, List["HybridWorkerQueueRequest"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        astro_runtime_version = self.astro_runtime_version
        cluster_id = self.cluster_id
        executor = self.executor.value

        is_cicd_enforced = self.is_cicd_enforced
        is_dag_deploy_enabled = self.is_dag_deploy_enabled
        name = self.name
        scheduler = self.scheduler.to_dict()

        type = self.type.value

        workspace_id = self.workspace_id
        description = self.description
        task_pod_node_pool_id = self.task_pod_node_pool_id
        worker_queues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.worker_queues, Unset):
            worker_queues = []
            for worker_queues_item_data in self.worker_queues:
                worker_queues_item = worker_queues_item_data.to_dict()

                worker_queues.append(worker_queues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "astroRuntimeVersion": astro_runtime_version,
                "clusterId": cluster_id,
                "executor": executor,
                "isCicdEnforced": is_cicd_enforced,
                "isDagDeployEnabled": is_dag_deploy_enabled,
                "name": name,
                "scheduler": scheduler,
                "type": type,
                "workspaceId": workspace_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if task_pod_node_pool_id is not UNSET:
            field_dict["taskPodNodePoolId"] = task_pod_node_pool_id
        if worker_queues is not UNSET:
            field_dict["workerQueues"] = worker_queues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_instance_spec_request import DeploymentInstanceSpecRequest
        from ..models.hybrid_worker_queue_request import HybridWorkerQueueRequest

        d = src_dict.copy()
        astro_runtime_version = d.pop("astroRuntimeVersion")

        cluster_id = d.pop("clusterId")

        executor = CreateHybridDeploymentRequestExecutor(d.pop("executor"))

        is_cicd_enforced = d.pop("isCicdEnforced")

        is_dag_deploy_enabled = d.pop("isDagDeployEnabled")

        name = d.pop("name")

        scheduler = DeploymentInstanceSpecRequest.from_dict(d.pop("scheduler"))

        type = CreateHybridDeploymentRequestType(d.pop("type"))

        workspace_id = d.pop("workspaceId")

        description = d.pop("description", UNSET)

        task_pod_node_pool_id = d.pop("taskPodNodePoolId", UNSET)

        worker_queues = []
        _worker_queues = d.pop("workerQueues", UNSET)
        for worker_queues_item_data in _worker_queues or []:
            worker_queues_item = HybridWorkerQueueRequest.from_dict(worker_queues_item_data)

            worker_queues.append(worker_queues_item)

        create_hybrid_deployment_request = cls(
            astro_runtime_version=astro_runtime_version,
            cluster_id=cluster_id,
            executor=executor,
            is_cicd_enforced=is_cicd_enforced,
            is_dag_deploy_enabled=is_dag_deploy_enabled,
            name=name,
            scheduler=scheduler,
            type=type,
            workspace_id=workspace_id,
            description=description,
            task_pod_node_pool_id=task_pod_node_pool_id,
            worker_queues=worker_queues,
        )

        create_hybrid_deployment_request.additional_properties = d
        return create_hybrid_deployment_request

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
