from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.client import Client
from ..models.order import Order
from ..models.readable_user import ReadableUser
from ..models.recurrence import Recurrence
from ..models.task import Task

T = TypeVar("T", bound="RecurrenceListScene")


@attr.s(auto_attribs=True)
class RecurrenceListScene:
    """
    Attributes:
        clients (List[Client]):
        orders (List[Order]):
        tasks (List[Task]):
        assignees (List[ReadableUser]):
        recurrences (List[Recurrence]):
    """

    clients: List[Client]
    orders: List[Order]
    tasks: List[Task]
    assignees: List[ReadableUser]
    recurrences: List[Recurrence]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clients = []
        for clients_item_data in self.clients:
            clients_item = clients_item_data.to_dict()

            clients.append(clients_item)

        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()

            orders.append(orders_item)

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()

            tasks.append(tasks_item)

        assignees = []
        for assignees_item_data in self.assignees:
            assignees_item = assignees_item_data.to_dict()

            assignees.append(assignees_item)

        recurrences = []
        for recurrences_item_data in self.recurrences:
            recurrences_item = recurrences_item_data.to_dict()

            recurrences.append(recurrences_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clients": clients,
                "orders": orders,
                "tasks": tasks,
                "assignees": assignees,
                "recurrences": recurrences,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clients = []
        _clients = d.pop("clients")
        for clients_item_data in _clients:
            clients_item = Client.from_dict(clients_item_data)

            clients.append(clients_item)

        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        assignees = []
        _assignees = d.pop("assignees")
        for assignees_item_data in _assignees:
            assignees_item = ReadableUser.from_dict(assignees_item_data)

            assignees.append(assignees_item)

        recurrences = []
        _recurrences = d.pop("recurrences")
        for recurrences_item_data in _recurrences:
            recurrences_item = Recurrence.from_dict(recurrences_item_data)

            recurrences.append(recurrences_item)

        recurrence_list_scene = cls(
            clients=clients,
            orders=orders,
            tasks=tasks,
            assignees=assignees,
            recurrences=recurrences,
        )

        recurrence_list_scene.additional_properties = d
        return recurrence_list_scene

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
