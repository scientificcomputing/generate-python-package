"""Top-level package for {{ cookiecutter.project_name }}."""
from importlib.metadata import metadata

meta = metadata("{{cookiecutter.module_name}}")
__version__ = meta["Version"]
__author__ = meta["Author"]
__license__ = meta["License"]
__email__ = meta["Author-email"]
__program_name__ = meta["Name"]
