
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
    'docs/api.rst',
    'docs/logo.png',
    'docs',
    '_config.yml',
    '_toc.yml',
    'index.md',
    {% endif %}
    {%- if cookiecutter.docker|lower != "y" %}
    'Dockerfile',
    '.github/workflows/docker-image.yml',
    "docker/Dockerfile",
    "docker",
    {% endif %}
    {%- if cookiecutter.use_argparse|lower != "y" %}
    'src/{{ cookiecutter.module_name }}/__main__.py',
    'src/{{ cookiecutter.module_name }}/cli.py',
    {% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
