from enum import Enum


class CreateStandardDeploymentRequestSchedulerSize(str, Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
