from pathlib import Path

class BaseConfig:
    def __init__(self, input_config:str):
        self.input_config = input_config
        self.config = None
        self.parse_config()
        

    @classmethod
    def load_config_from_file(cls, filename:str):
        path = Path(filename)

        if path.exists():
            with path.open("r") as config_file:
                config = config_file.read() 
                return cls(config)
        else:
            raise FileNotFoundError(f"No such file '{path}'")

    def parse_config(self):
        print(self.input_config)
        self.config = self.input_config 
