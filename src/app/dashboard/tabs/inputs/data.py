from enum import Enum
from pathlib import Path
import json

class Flowcharts(Enum):
    DEMO = 1

FLOWCHART_FILES = {
    Flowcharts.DEMO: "data/demo.json"
}

def list_flowchart_names():
    return [flow.name for flow in Flowcharts]

def read_flowchart(name:str) -> str:
    if name in Flowcharts:
        name = name.name
    if name in list_flowchart_names():
        fpath = Path(__file__).parent / FLOWCHART_FILES[Flowcharts[name]]
        return json.load(open(fpath, "r"))
    else:
        raise NameError(f"Flowchart file {name} does not exist")