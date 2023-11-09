from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterMetadata")


@_attrs_define
class ClusterMetadata:
    """
    Attributes:
        external_i_ps (Union[Unset, List[str]]): External IPs of the cluster. Example: ['35.100.100.1'].
    """

    external_i_ps: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_i_ps: Union[Unset, List[str]] = UNSET
        if not isinstance(self.external_i_ps, Unset):
            external_i_ps = self.external_i_ps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_i_ps is not UNSET:
            field_dict["externalIPs"] = external_i_ps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_i_ps = cast(List[str], d.pop("externalIPs", UNSET))

        cluster_metadata = cls(
            external_i_ps=external_i_ps,
        )

        cluster_metadata.additional_properties = d
        return cluster_metadata

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
