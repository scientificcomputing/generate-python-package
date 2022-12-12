#!/usr/bin/env python

from {{cookiecutter.module_name}}.cli import main
{% if cookiecutter.command_line_interface|lower != 'none' -%}
if __name__ == "__main__":
    {% if cookiecutter.command_line_interface|lower == 'typer' -%}
    import typer
    typer.run(main)
    {% else -%}
    import sys
    sys.exit(main())
    {% endif -%}
{% endif -%}
