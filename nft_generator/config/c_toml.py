import toml

from nft_generator.config import BaseConfig

class TomlConfig(BaseConfig):
    def parse_config(self):
        self.config = toml.loads(self.input_config)
        return self.config

