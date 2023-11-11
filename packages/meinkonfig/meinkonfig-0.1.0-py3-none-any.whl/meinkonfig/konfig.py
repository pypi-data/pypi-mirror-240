import os
import re
import yaml
import dotenv
import pathlib
from easydict import EasyDict
from typing import Any


class Konfig:
    def __init__(self, path: str, konfig_file: str):
        self.path = path
        self.konfig_file = konfig_file

    def load_konfig(self):
        dotenv.load_dotenv('.env')
        self.load_file()

    def load_file(self):
        try:
            file_path = pathlib.Path(self.path, self.konfig_file)
            with open(file_path, 'r') as file:
                if file_path.suffix == '.yaml':
                    cfg = yaml.safe_load(file)
            self.set_konfig(cfg)
        except Exception as err:
            raise err

    def set_konfig(self, cfg: dict):
        cfg = load_env_variables(cfg)
        setattr(self, self.konfig_file.split('.')[0], EasyDict(cfg))


def load_env_variables(node: Any) -> Any:
    if isinstance(node, (dict, EasyDict)):
        for k, v in node.items():
            node[k] = load_env_variables(v)
        return node
    elif isinstance(node, list):
        return [load_env_variables(n) for n in node]
    elif isinstance(node, str):
        for env in re.findall(r"\$\w+", node):
            val = os.environ.get(env[1:], None)
            if val is not None:
                node = node.replace(env, val)
        return node
    else:
        return node
