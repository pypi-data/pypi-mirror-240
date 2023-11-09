from enum import Enum


class DeploymentExecutor(str, Enum):
    CELERY = "CELERY"
    KUBERNETES = "KUBERNETES"

    def __str__(self) -> str:
        return str(self.value)
