import shutil
from pathlib import Path

import pytest

from tests.utils.project import generate_project


def test__can_generate_project(project_dir: Path):
    """
    execute test cookiecutter
    """
    assert project_dir.exists()
