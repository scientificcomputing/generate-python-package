import pytest
from pathlib import Path
import sys
import subprocess as sp


@pytest.fixture
def python_venv(tmp_path) -> str:
    """Create a new python virtual environment
    and return the path to the python executable
    """
    python = sys.executable
    # Create virual environment
    sp.run([python, "-m", "venv", tmp_path.as_posix()])
    yield (tmp_path / "bin" / "python").as_posix()


def test_bake_project(cookies, python_venv):
    result = cookies.bake(extra_context={"repository_name": "my_project"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my_project"
    assert result.project_path.is_dir()

    assert result.project.basename == "my_project"
    assert result.project.isdir()

    # Try to install the the package and run the tests
    result.project.chdir()
    res_install = sp.run(
        [python_venv, "-m", "pip", "install", ".[test]"], capture_output=True
    )
    assert res_install.returncode == 0, res_install.stderr

    res_pytest = sp.run([python_venv, "-m", "pytest"], capture_output=True)
    assert res_pytest.returncode == 0, res_pytest.stderr

    # Install pre-commit
    result.project.chdir()
    res_install = sp.run(
        [python_venv, "-m", "pip", "install", "pre-commit"], capture_output=True
    )
    assert res_install.returncode == 0, res_install.stderr
    pre_commit = Path(python_venv).with_name("pre-commit").as_posix()
    # Initialize git repo
    sp.run(["git", "init"], capture_output=True)
    # Add all files
    sp.run(["git", "add", "."], capture_output=True)
    res_pre_commit = sp.run([pre_commit, "run", "--all"], capture_output=True)
    diff_file = Path.cwd().absolute() / "diff.txt"
    sp.run(["git", "diff", f"--output={diff_file.as_posix()}"], capture_output=True)
    diff = diff_file.read_text()
    diff_file.unlink()
    assert res_pre_commit.returncode == 0, diff
