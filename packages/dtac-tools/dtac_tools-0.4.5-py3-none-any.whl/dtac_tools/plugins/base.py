import json
from pydantic import BaseModel
from typing import TypeVar, Type

# Base Config class, this is used to help deserialize configuration options for plugins
class BaseConfig(BaseModel):
    pass


class PluginShared:
    @staticmethod
    def name() -> str:
        return "UnnamedPlugin"
    
    @staticmethod
    def route_root() -> str:
        return ""
    
    @staticmethod
    def serialize(v: object) -> str:
        return json.dumps(v)

class PluginBase(PluginShared):

    T = TypeVar("T", bound=BaseConfig)

    def load_config(self, config_json: str, config_class: Type[T]) -> T:
        return config_class.parse_raw(config_json)

    def register(self, args):
        raise NotImplementedError("this method must be implemented")
