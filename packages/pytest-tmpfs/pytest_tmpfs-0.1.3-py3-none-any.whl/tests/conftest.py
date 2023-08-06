"""Test setup for TmpFs."""
from pathlib import Path
import pytest


@pytest.fixture(autouse=True)
def add_tmp_path(doctest_namespace: dict, tmp_path: Path):
    """Adds the temporary file system to the doctest namespace."""
    doctest_namespace["tmp_path"] = tmp_path
