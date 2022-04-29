from enum import Enum


class ExportModelEnum(str, Enum):
    TASKS = "tasks"

    def __str__(self) -> str:
        return str(self.value)
