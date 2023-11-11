from typing import Any

from typytemplate.templates import formatted


@formatted
def format_file(**kwargs: dict[str, Any]) -> str:
    """Formats the 'pyproject.toml' file with provided configuration"""
    return f"""
        [tool.poetry]
        name = "{kwargs["package_name"]}"
        version = "{kwargs["version"]}"
        description = "{kwargs["description"]}"
        license = "{kwargs["license"]}"
        authors = ["{kwargs["author"]}"]
        readme = "README.md"
        packages = [{{include = "{kwargs["package_name"]}"}}]


        [tool.poetry.scripts]
        {kwargs["package_name"]} = "{kwargs["package_name"]}.main:main"


        [tool.poetry.dependencies]
        python = "^{kwargs["python_version"]}"


        [tool.ruff]
        line-length = {kwargs["line_length"]}


        [tool.pylint."MESSAGES CONTROL"]
        max-line-length = 120
        disable = [
            "C0114", # missing-module-docstring
            "C0115", # missing-class-docstring
            "C0116", # missing-function-docstring
        ]
        good-names = ["i"]
        ignored-modules=""


        [tool.pytest.ini_options]
        pythonpath = ["."]


        [tool.mypy]
        strict = true
        exclude = ["tests"]


        [build-system]
        requires = ["poetry-core"]
        build-backend = "poetry.core.masonry.api"
    """
