from typing import Protocol


class ILogger(Protocol):
    def log(self, msg: str) -> None:
        ...
