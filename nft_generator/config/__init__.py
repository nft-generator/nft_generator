from pathlib import Path

class BaseConfig:
    def __init__(self, data:str):
        self.data = data
        self.parse_data()
    def load_config_from_file(filename:str):
        Path