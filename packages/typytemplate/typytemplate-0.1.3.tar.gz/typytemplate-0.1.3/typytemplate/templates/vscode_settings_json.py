from typing import Any

from typytemplate.templates import formatted


@formatted
def format_file(**kwargs: dict[str, Any]) -> str:
    """Formats the VSCode 'settings.json' file with basic configuration"""
    return f"""
        {{
            "editor.rulers": [
                {kwargs["line_length"]}
            ],
            "[python]": {{
                "editor.defaultFormatter": "charliermarsh.ruff",
                "editor.formatOnSave": true,
                "editor.codeActionsOnSave": {{
                    "source.organizeImports.ruff": true
                }},
            }},
            "mypy-type-checker.args": [
                "--config-file=${{workspaceFolder}}/pyproject.toml"
            ],
            "python.envFile": "${{workspaceFolder}}/.venv",
            "python.defaultInterpreterPath": "${{workspaceFolder}}/.venv/bin/python",
            "python.analysis.typeCheckingMode": "strict",
            "python.analysis.diagnosticSeverityOverrides": {{
                "reportPrivateUsage": "information",
                "reportMissingTypeStubs": "information",
            }},
        }}
    """
