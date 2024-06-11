"""Test project creation."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """
    execute test cookiecutter
    """
    assert project_dir.exists()
