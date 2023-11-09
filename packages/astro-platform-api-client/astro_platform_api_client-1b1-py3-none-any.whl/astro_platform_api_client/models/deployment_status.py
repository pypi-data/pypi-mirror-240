from enum import Enum


class DeploymentStatus(str, Enum):
    CREATING = "CREATING"
    DEPLOYING = "DEPLOYING"
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
