#!/usr/bin/env python
from {{cookiecutter.module_name}}.cli import main

{% if cookiecutter.command_line_interface|lower != 'none' -%}
{% if cookiecutter.command_line_interface|lower == 'typer' -%}
if __name__ == "__main__":
    import typer

    typer.run(main)
{% else -%}
if __name__ == "__main__":
    import sys

    sys.exit(main())
{% endif -%}
{% endif -%}