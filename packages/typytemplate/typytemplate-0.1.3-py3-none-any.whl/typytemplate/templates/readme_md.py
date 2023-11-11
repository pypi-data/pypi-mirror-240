from typing import Any

from typytemplate.templates import formatted


@formatted
def format_file(**kwargs: dict[str, Any]) -> str:
    """Formats the 'README.md' file with basic project description"""
    return f"""
        # {kwargs["package_name"]}

        {kwargs["description"]}

        🔨 **WIP**
    """
