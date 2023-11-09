from enum import Enum


class WorkerQueueRequestAstroMachine(str, Enum):
    A10 = "A10"
    A20 = "A20"
    A40 = "A40"
    A5 = "A5"
    A60 = "A60"

    def __str__(self) -> str:
        return str(self.value)
