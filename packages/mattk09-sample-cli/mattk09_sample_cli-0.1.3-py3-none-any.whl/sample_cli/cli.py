import logging
from typing import Any

import click

import sample_cli.app as app

from .config import get_config
from .contracts import ILogger

config = get_config()


class ClickLogger(ILogger):
    def log(self, log: str) -> None:
        click.echo(log)


class DefaultLogger(ILogger):
    def __init__(self, log_level: int) -> None:
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(log_level)

    def log(self, log: str) -> None:
        self._logger.info(log)


@click.command()
@click.option("--count", default=config["default_count"], help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(count: int, name: str, **kwargs: Any) -> None:
    """Simple program that greets NAME for a total of COUNT times."""

    app.main(count, name, logger=ClickLogger(), **kwargs)


@click.command()
def hello() -> None:
    app.hello(logger=DefaultLogger(config["logging"]["level"]))


if __name__ == "__main__":
    main()
