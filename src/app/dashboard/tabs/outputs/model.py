from enum import Enum
from pathlib import Path

from .fileutils import read_file
class Models(Enum):
    FLOATING = 1

MODEL_FILES = {
    Models.FLOATING: "models/floating.ifc"
}

def list_model_names():
    return [model.name for model in Models]

def read_model(name:str) -> str:
    if name in list_model_names():
        fpath = Path(__file__).parent / MODEL_FILES[Models[name]]
        return fpath.name, read_file(fpath)
    else:
        raise NameError(f"Model name {name} does not exist")