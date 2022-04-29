from enum import Enum


class State29FEnum(str, Enum):
    UNKNOWN = "unknown"
    STOPPED = "stopped"
    MOVING = "moving"

    def __str__(self) -> str:
        return str(self.value)
