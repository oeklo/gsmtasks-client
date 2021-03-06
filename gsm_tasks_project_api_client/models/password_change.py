from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="PasswordChange")


@attr.s(auto_attribs=True)
class PasswordChange:
    """
    Attributes:
        old_password (str):
        new_password1 (str):
        new_password2 (str):
    """

    old_password: str
    new_password1: str
    new_password2: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old_password = self.old_password
        new_password1 = self.new_password1
        new_password2 = self.new_password2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_password": old_password,
                "new_password1": new_password1,
                "new_password2": new_password2,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        old_password = (
            self.old_password
            if isinstance(self.old_password, Unset)
            else (None, str(self.old_password).encode(), "text/plain")
        )
        new_password1 = (
            self.new_password1
            if isinstance(self.new_password1, Unset)
            else (None, str(self.new_password1).encode(), "text/plain")
        )
        new_password2 = (
            self.new_password2
            if isinstance(self.new_password2, Unset)
            else (None, str(self.new_password2).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "old_password": old_password,
                "new_password1": new_password1,
                "new_password2": new_password2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old_password = d.pop("old_password")

        new_password1 = d.pop("new_password1")

        new_password2 = d.pop("new_password2")

        password_change = cls(
            old_password=old_password,
            new_password1=new_password1,
            new_password2=new_password2,
        )

        password_change.additional_properties = d
        return password_change

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
