from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateOrganizationRequest")


@_attrs_define
class UpdateOrganizationRequest:
    """
    Attributes:
        billing_email (str): The Organization's billing email. Example: billing@company.com.
        is_scim_enabled (bool): Whether SCIM is enabled for the Organization.
        name (str): The name of the Organization. Example: My Organization.
    """

    billing_email: str
    is_scim_enabled: bool
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_email = self.billing_email
        is_scim_enabled = self.is_scim_enabled
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingEmail": billing_email,
                "isScimEnabled": is_scim_enabled,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_email = d.pop("billingEmail")

        is_scim_enabled = d.pop("isScimEnabled")

        name = d.pop("name")

        update_organization_request = cls(
            billing_email=billing_email,
            is_scim_enabled=is_scim_enabled,
            name=name,
        )

        update_organization_request.additional_properties = d
        return update_organization_request

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
