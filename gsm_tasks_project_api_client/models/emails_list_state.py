from enum import Enum


class EmailsListState(str, Enum):
    QUEUED = "queued"
    OVER_QUOTA = "over_quota"
    SENT = "sent"
    FAILED = "failed"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
