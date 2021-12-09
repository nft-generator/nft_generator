from nft_generator.config.base import BaseConfig


from nft_generator.config.c_toml import TomlConfig
from nft_generator.config.c_json import JsonConfig
from nft_generator.config.c_yaml import YamlConfig

def load_config_from_file(filename:str):
    ext = filename.split(".")[1]
    if ext == "yml" or ext == "yaml":
        return YamlConfig.load_config_from_file(filename)
    elif ext == "toml":
        return TomlConfig.load_config_from_file(filename)
    elif ext == "json":
        return JsonConfig.load_config_from_file(filename)