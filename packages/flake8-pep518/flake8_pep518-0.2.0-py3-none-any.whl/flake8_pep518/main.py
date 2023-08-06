import flake8.options.config

import flake8_pep518.mixins as mixins


class Plugin:
    def add_options(self) -> None:
        flake8.options.config.parse_config = mixins.parse_config_toml
