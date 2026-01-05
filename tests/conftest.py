"""Shared test fixtures for crewai-fs-plus tests."""

import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_files(temp_dir: Path) -> Path:
    """Create a sample file structure for testing.

    Structure:
        temp_dir/
        ├── file1.txt
        ├── file2.py
        ├── secret.txt
        ├── .env
        ├── docs/
        │   ├── readme.md
        │   └── guide.txt
        ├── src/
        │   ├── main.py
        │   └── utils.py
        └── output/
            └── result.txt
    """
    # Create directories
    (temp_dir / "docs").mkdir()
    (temp_dir / "src").mkdir()
    (temp_dir / "output").mkdir()

    # Create files with content
    files = {
        "file1.txt": "Hello World\nLine 2\nLine 3\n",
        "file2.py": "print('hello')\n",
        "secret.txt": "secret data\n",
        ".env": "API_KEY=secret123\n",
        "docs/readme.md": "# Documentation\n\nWelcome!\n",
        "docs/guide.txt": "Guide content\n",
        "src/main.py": "def main():\n    pass\n",
        "src/utils.py": "def helper():\n    return True\n",
        "output/result.txt": "Result output\n",
    }

    for filepath, content in files.items():
        (temp_dir / filepath).write_text(content)

    return temp_dir


@pytest.fixture
def empty_dir(temp_dir: Path) -> Path:
    """Create an empty directory for testing."""
    empty = temp_dir / "empty_dir"
    empty.mkdir()
    return empty
