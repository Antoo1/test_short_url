from ruamel.yaml import YAML
from pydantic import BaseModel


yaml_loader = YAML(typ='safe')


class ConfigFactory:
    def __init__(self, config_model: BaseModel):
        self._model = config_model

    def from_file(self, filename, loader=yaml_loader) -> BaseModel:

        with open(filename) as f:
            raw_data = loader.load(f)
            return self._model.parse_obj(raw_data)
