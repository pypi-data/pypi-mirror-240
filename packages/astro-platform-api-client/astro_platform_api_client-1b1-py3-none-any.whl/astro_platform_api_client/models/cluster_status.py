from enum import Enum


class ClusterStatus(str, Enum):
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"

    def __str__(self) -> str:
        return str(self.value)
