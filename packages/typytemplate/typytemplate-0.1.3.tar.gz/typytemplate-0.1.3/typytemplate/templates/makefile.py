from typing import Any

from typytemplate.templates import formatted


@formatted
def format_file(**kwargs: dict[str, Any]) -> str:
    """Formats the 'Makefile' file with basic commands"""
    return f"""
        run:
        \tpoetry run python -m {kwargs["package_name"]}.main

        test:
        \tpoetry run coverage run --source={kwargs["package_name"]} -m pytest -vv
        \tpoetry run coverage report --show-missing --skip-empty

        lint:
        \tpoetry run ruff ./
        \tpoetry run pylint ./{kwargs["package_name"]}
        \tpoetry run mypy . --explicit-package-bases

        install:
        \tpoetry install
    """
