from enum import Enum


class MetafieldsListValueType(str, Enum):
    STRING = "string"
    INTEGER = "integer"
    DECIMAL = "decimal"
    CHOICE = "choice"

    def __str__(self) -> str:
        return str(self.value)
