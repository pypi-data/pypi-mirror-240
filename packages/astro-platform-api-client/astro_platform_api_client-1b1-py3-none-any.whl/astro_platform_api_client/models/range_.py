from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Range")


@_attrs_define
class Range:
    """
    Attributes:
        ceiling (float): The maximum value. Example: 10.
        default (float): The default value. Example: 5.
        floor (float): The minimum value. Example: 1.
    """

    ceiling: float
    default: float
    floor: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ceiling = self.ceiling
        default = self.default
        floor = self.floor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ceiling": ceiling,
                "default": default,
                "floor": floor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ceiling = d.pop("ceiling")

        default = d.pop("default")

        floor = d.pop("floor")

        range_ = cls(
            ceiling=ceiling,
            default=default,
            floor=floor,
        )

        range_.additional_properties = d
        return range_

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
