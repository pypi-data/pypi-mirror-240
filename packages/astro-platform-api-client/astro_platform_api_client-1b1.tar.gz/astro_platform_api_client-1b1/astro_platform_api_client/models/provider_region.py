from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderRegion")


@_attrs_define
class ProviderRegion:
    """
    Attributes:
        name (str): The name of the region. Example: us-east-1.
        banned_instances (Union[Unset, List[str]]): The banned instances in the region. Example: ['t3.medium'].
        limited (Union[Unset, bool]): Whether the region is limited. Example: True.
    """

    name: str
    banned_instances: Union[Unset, List[str]] = UNSET
    limited: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        banned_instances: Union[Unset, List[str]] = UNSET
        if not isinstance(self.banned_instances, Unset):
            banned_instances = self.banned_instances

        limited = self.limited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if banned_instances is not UNSET:
            field_dict["bannedInstances"] = banned_instances
        if limited is not UNSET:
            field_dict["limited"] = limited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        banned_instances = cast(List[str], d.pop("bannedInstances", UNSET))

        limited = d.pop("limited", UNSET)

        provider_region = cls(
            name=name,
            banned_instances=banned_instances,
            limited=limited,
        )

        provider_region.additional_properties = d
        return provider_region

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
