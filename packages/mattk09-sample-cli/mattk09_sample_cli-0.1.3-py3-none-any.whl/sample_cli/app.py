import os
from typing import Any

from .contracts import ILogger


def main(count: int, name: str, logger: ILogger, **kwargs: Any) -> None:
    """Simple program that greets NAME for a total of COUNT times."""

    logger.log(f"name: {name}, count: {count}")

    for x in range(count):
        print(f"Hello {name}!")


def hello(logger: ILogger) -> None:
    logger.log(f"Hello, {os.getpid()}!")
    print(f"Hello, {os.getpid()}!")
