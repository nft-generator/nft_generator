import yaml

from nft_generator.config import BaseConfig

class YamlConfig(BaseConfig):
    def parse_config(self):
        self.config = yaml.safe_load(self.input_config)
        return self.config
