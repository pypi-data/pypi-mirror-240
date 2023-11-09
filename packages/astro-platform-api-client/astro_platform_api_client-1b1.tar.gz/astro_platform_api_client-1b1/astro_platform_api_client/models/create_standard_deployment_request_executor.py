from enum import Enum


class CreateStandardDeploymentRequestExecutor(str, Enum):
    CELERY = "CELERY"
    KUBERNETES = "KUBERNETES"

    def __str__(self) -> str:
        return str(self.value)
