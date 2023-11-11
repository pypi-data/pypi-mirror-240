import importlib.resources
from typing import Any, Dict

import tomli


def get_config() -> Dict[str, Any]:
    with importlib.resources.open_binary("sample_cli", "sample-cli.toml") as file:
        return tomli.load(file)
