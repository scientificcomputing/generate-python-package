
import os

REMOVE_PATHS = [
    {%- if cookiecutter.testing|lower == "none" %}
    'tests/test_version.py',
    'tests/',
    '.github/workflows/test_package.yml',
    {%- elif cookiecutter.testing|lower == "pytest" %}
    '.github/workflows/test_package_coverage.yml',
    {%- elif cookiecutter.testing|lower == "pytest-cov" %}
    '.github/workflows/test_package.yml',
    {%- endif %}
    {%- if cookiecutter.linting|lower != "y" %}
    '.github/workflows/check_formatting.yml',
    '.flake8',
    '.github/workflows/build_docs.yml',
    'docs/_config.yml',
    'docs/_toc.yml',
    'docs/api.rst',
    'docs/index.md',
    'docs/logo.png',
    'docs'
    {% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
