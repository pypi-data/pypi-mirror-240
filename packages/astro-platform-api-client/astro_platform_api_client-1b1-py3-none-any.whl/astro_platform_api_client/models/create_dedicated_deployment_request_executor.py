from enum import Enum


class CreateDedicatedDeploymentRequestExecutor(str, Enum):
    CELERY = "CELERY"
    KUBERNETES = "KUBERNETES"

    def __str__(self) -> str:
        return str(self.value)
