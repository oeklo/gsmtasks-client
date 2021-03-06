import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.patched_recurrence_tasks_data import PatchedRecurrenceTasksData
from ..models.timezone_enum import TimezoneEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRecurrence")


@attr.s(auto_attribs=True)
class PatchedRecurrence:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        order (Union[Unset, str]):
        assign_worker (Union[Unset, bool]):
        is_active (Union[Unset, bool]):  Default: True.
        rrule (Union[Unset, str]):
        timezone (Union[Unset, TimezoneEnum]):
        last_recurred_at (Union[Unset, datetime.datetime]):
        last_scheduled_at (Union[Unset, datetime.datetime]):
        next_scheduled_at (Union[Unset, datetime.datetime]):
        tasks_data (Union[Unset, PatchedRecurrenceTasksData]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    assign_worker: Union[Unset, bool] = False
    is_active: Union[Unset, bool] = True
    rrule: Union[Unset, str] = UNSET
    timezone: Union[Unset, TimezoneEnum] = UNSET
    last_recurred_at: Union[Unset, datetime.datetime] = UNSET
    last_scheduled_at: Union[Unset, datetime.datetime] = UNSET
    next_scheduled_at: Union[Unset, datetime.datetime] = UNSET
    tasks_data: Union[Unset, PatchedRecurrenceTasksData] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        order = self.order
        assign_worker = self.assign_worker
        is_active = self.is_active
        rrule = self.rrule
        timezone: Union[Unset, str] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.value

        last_recurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_recurred_at, Unset):
            last_recurred_at = self.last_recurred_at.isoformat()

        last_scheduled_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_scheduled_at, Unset):
            last_scheduled_at = self.last_scheduled_at.isoformat()

        next_scheduled_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_scheduled_at, Unset):
            next_scheduled_at = self.next_scheduled_at.isoformat()

        tasks_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            tasks_data = self.tasks_data.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if order is not UNSET:
            field_dict["order"] = order
        if assign_worker is not UNSET:
            field_dict["assign_worker"] = assign_worker
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if rrule is not UNSET:
            field_dict["rrule"] = rrule
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if last_recurred_at is not UNSET:
            field_dict["last_recurred_at"] = last_recurred_at
        if last_scheduled_at is not UNSET:
            field_dict["last_scheduled_at"] = last_scheduled_at
        if next_scheduled_at is not UNSET:
            field_dict["next_scheduled_at"] = next_scheduled_at
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        order = self.order if isinstance(self.order, Unset) else (None, str(self.order).encode(), "text/plain")
        assign_worker = (
            self.assign_worker
            if isinstance(self.assign_worker, Unset)
            else (None, str(self.assign_worker).encode(), "text/plain")
        )
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        rrule = self.rrule if isinstance(self.rrule, Unset) else (None, str(self.rrule).encode(), "text/plain")
        timezone: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = (None, str(self.timezone.value).encode(), "text/plain")

        last_recurred_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.last_recurred_at, Unset):
            last_recurred_at = self.last_recurred_at.isoformat().encode()

        last_scheduled_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.last_scheduled_at, Unset):
            last_scheduled_at = self.last_scheduled_at.isoformat().encode()

        next_scheduled_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.next_scheduled_at, Unset):
            next_scheduled_at = self.next_scheduled_at.isoformat().encode()

        tasks_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            tasks_data = (None, json.dumps(self.tasks_data.to_dict()).encode(), "application/json")

        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if order is not UNSET:
            field_dict["order"] = order
        if assign_worker is not UNSET:
            field_dict["assign_worker"] = assign_worker
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if rrule is not UNSET:
            field_dict["rrule"] = rrule
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if last_recurred_at is not UNSET:
            field_dict["last_recurred_at"] = last_recurred_at
        if last_scheduled_at is not UNSET:
            field_dict["last_scheduled_at"] = last_scheduled_at
        if next_scheduled_at is not UNSET:
            field_dict["next_scheduled_at"] = next_scheduled_at
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        order = d.pop("order", UNSET)

        assign_worker = d.pop("assign_worker", UNSET)

        is_active = d.pop("is_active", UNSET)

        rrule = d.pop("rrule", UNSET)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, TimezoneEnum]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = TimezoneEnum(_timezone)

        _last_recurred_at = d.pop("last_recurred_at", UNSET)
        last_recurred_at: Union[Unset, datetime.datetime]
        if isinstance(_last_recurred_at, Unset):
            last_recurred_at = UNSET
        else:
            last_recurred_at = isoparse(_last_recurred_at)

        _last_scheduled_at = d.pop("last_scheduled_at", UNSET)
        last_scheduled_at: Union[Unset, datetime.datetime]
        if isinstance(_last_scheduled_at, Unset):
            last_scheduled_at = UNSET
        else:
            last_scheduled_at = isoparse(_last_scheduled_at)

        _next_scheduled_at = d.pop("next_scheduled_at", UNSET)
        next_scheduled_at: Union[Unset, datetime.datetime]
        if isinstance(_next_scheduled_at, Unset):
            next_scheduled_at = UNSET
        else:
            next_scheduled_at = isoparse(_next_scheduled_at)

        _tasks_data = d.pop("tasks_data", UNSET)
        tasks_data: Union[Unset, PatchedRecurrenceTasksData]
        if isinstance(_tasks_data, Unset):
            tasks_data = UNSET
        else:
            tasks_data = PatchedRecurrenceTasksData.from_dict(_tasks_data)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patched_recurrence = cls(
            id=id,
            url=url,
            account=account,
            order=order,
            assign_worker=assign_worker,
            is_active=is_active,
            rrule=rrule,
            timezone=timezone,
            last_recurred_at=last_recurred_at,
            last_scheduled_at=last_scheduled_at,
            next_scheduled_at=next_scheduled_at,
            tasks_data=tasks_data,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_recurrence.additional_properties = d
        return patched_recurrence

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
