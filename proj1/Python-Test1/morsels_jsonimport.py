

from importlib.abc import Loader, MetaPathFinder
from importlib.util import module_from_spec, spec_from_loader
import json
from pathlib import Path
import sys


def import_json(name, paths):
    for directory in paths:
        json_path = Path(directory, f"{name}.json")
        if json_path.is_file():
            try:
                return json.loads(json_path.read_text())
            except ValueError as e:
                raise ImportError(f"JSON in {json_path!r} is malformed") from e
    return None

def import_json2(name, paths):
    for directory in paths:
        json_path = Path(directory, f"{name}.json")
        if json_path.is_file():
            try:
                with open(json_path) as f:
                    return json.load(f)
            except ValueError as e:
                raise ImportError(f"JSON in {json_path!r} is malformed") from e
    return None

class JSONFinder(MetaPathFinder):

    def find_spec(self, name, path=None, target=None):
        print (path)
        if path is None:
            path = sys.path
        for directory in path:
            module_name = name.rsplit('.', 1)[-1]
            print(name)
            print(module_name)
            json_path = Path(directory, f"{module_name}.json")
            print(json_path)
            if json_path.is_file():
                return spec_from_loader(name, JSONLoader(json_path))
        return None


class JSONLoader(Loader):

    def __init__(self, json_path):
        self.json_path = json_path

    def create_module(self, spec):
        try:
            print("create_module")
            #print(self.json_path.read_text())
            return json.loads(self.json_path.read_text())
        except ValueError as e:
            raise ImportError(f"{self.json_path!r} is malformed") from e

    def exec_module(self, module):
        """JSON object already exists and doesn't need to be executed."""

print(import_json('instanceMapping', ['data']))
print(import_json2('instanceMapping', ['data']))

sys.meta_path.append(JSONFinder())
print(sys.meta_path)
from data import instanceMapping


