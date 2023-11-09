from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.range_ import Range


T = TypeVar("T", bound="WorkerQueueOptions")


@_attrs_define
class WorkerQueueOptions:
    """
    Attributes:
        max_workers (Range):
        min_workers (Range):
        worker_concurrency (Range):
    """

    max_workers: "Range"
    min_workers: "Range"
    worker_concurrency: "Range"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_workers = self.max_workers.to_dict()

        min_workers = self.min_workers.to_dict()

        worker_concurrency = self.worker_concurrency.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxWorkers": max_workers,
                "minWorkers": min_workers,
                "workerConcurrency": worker_concurrency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_ import Range

        d = src_dict.copy()
        max_workers = Range.from_dict(d.pop("maxWorkers"))

        min_workers = Range.from_dict(d.pop("minWorkers"))

        worker_concurrency = Range.from_dict(d.pop("workerConcurrency"))

        worker_queue_options = cls(
            max_workers=max_workers,
            min_workers=min_workers,
            worker_concurrency=worker_concurrency,
        )

        worker_queue_options.additional_properties = d
        return worker_queue_options

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
