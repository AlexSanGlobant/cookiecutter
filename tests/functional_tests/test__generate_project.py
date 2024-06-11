"""Test project creation."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Execute test cookiecutter."""
    assert project_dir.exists()
