"""Integration tests for the package."""

import subprocess
import sys
from pathlib import Path
from typing import List, Union

import pytest


def run_flake8(fixture: str, args: Union[List[str], None] = None):
    folder = Path(__file__).parent / "fixtures" / fixture
    process = subprocess.run(
        [sys.executable, "-m", "flake8", ".", *(args or [])],
        cwd=folder,
        stdout=subprocess.PIPE,
        text=True,
    )
    results = process.stdout.strip().split("\n")
    return results


@pytest.mark.parametrize(
    "fixture, expected",
    [
        ("empty_folder", [""]),
        ("empty_pyproject", [""]),
        (
            "default",
            [
                "./module.py:5:14: E221 multiple spaces before operator",
                "./module.py:6:32: W292 no newline at end of file",
                "2",
            ],
        ),
    ],
)
def test_flake8(fixture: str, expected: List[str]):
    results = run_flake8(fixture)
    assert results == expected
