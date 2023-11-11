from typing import Any

from typytemplate.templates import formatted


@formatted
def format_file(**kwargs: dict[str, Any]) -> str:
    """Formats the 'pyproject.toml' file with provided configuration"""
    return f"""
        from {kwargs["package_name"]} import main


        class TestMain:
            def test_main(self) -> None:
                assert main.main() == 0
    """
