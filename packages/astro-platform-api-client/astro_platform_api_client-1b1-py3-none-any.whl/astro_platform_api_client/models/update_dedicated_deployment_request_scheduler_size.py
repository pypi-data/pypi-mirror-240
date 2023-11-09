from enum import Enum


class UpdateDedicatedDeploymentRequestSchedulerSize(str, Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
