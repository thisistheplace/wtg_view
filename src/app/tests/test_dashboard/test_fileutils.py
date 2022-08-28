import os
from pathlib import Path
import pytest
import shutil
from uuid import uuid4

ROOT = Path(__file__).parent

from app.dashboard.fileutils import read_wasm

@pytest.fixture
def test_dir() -> Path:
    test_dir = ROOT / str(uuid4())
    os.makedirs(test_dir)
    yield test_dir
    shutil.rmtree(test_dir)

@pytest.fixture
def wasm_path(test_dir: Path) -> Path:
    wasm_path = test_dir / "test.wasm"
    wasm_path.touch()
    yield wasm_path

class TestReadWasm:
    def test_wasm_exists(self, wasm_path: Path):
        assert wasm_path.exists()
        assert isinstance(read_wasm(wasm_path), bytes)