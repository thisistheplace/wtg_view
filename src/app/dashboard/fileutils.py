from pathlib import Path

def read_wasm(fpath: str) -> bytes:
    resolved = Path(fpath).resolve()
    with open(resolved, "rb") as f:
        fbytes = f.read()
    return fbytes