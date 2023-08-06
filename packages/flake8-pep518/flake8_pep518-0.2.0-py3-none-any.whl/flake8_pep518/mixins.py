import sys
from pathlib import Path
from typing import Any, Dict, Union

from flake8.options.config import OptionManager, configparser, parse_config

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib  # pragma: no cover


def create_parser(file: Path) -> Union[configparser.RawConfigParser, None]:
    if not file.exists():
        return None
    with file.open("rb") as stream:
        settings = tomllib.load(stream)
    if "tool" not in settings or "flake8" not in settings["tool"]:
        return None
    parser = configparser.RawConfigParser()
    parser.add_section("flake8")
    for (key, value) in settings["tool"]["flake8"].items():
        if isinstance(value, (bool, int, float)):
            value = str(value)
        parser.set("flake8", key, value)
    return parser


def parse_config_toml(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> Dict[str, Any]:
    return parse_config(  # type: ignore[no-any-return]
        option_manager,
        create_parser(Path(cfg_dir) / "pyproject.toml") or cfg,
        cfg_dir,
    )
