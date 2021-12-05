import json

from nft_generator.config import BaseConfig

class JsonConfig(BaseConfig):
    def parse_config(self):
        self.config = json.loads(self.input_config)
        
