import base64
from pathlib import Path

def read_file(fpath: str) -> str:
    resolved = Path(fpath).resolve()
    with open(resolved, "r") as f:
        fstring = f.read()
    return fstring

def parse_contents(contents: str, filename: str) -> str:
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'ifc' in filename.lower():
        return decoded.decode('utf-8')
    else:
        raise TypeError("Only .IFC file extensions are supported!")