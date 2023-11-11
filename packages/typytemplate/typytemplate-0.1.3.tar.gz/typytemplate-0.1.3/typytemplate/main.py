import argparse
import os
import subprocess
import sys
from os.path import join as path_join
from subprocess import Popen
from typing import Any

from typytemplate.templates import (
    dot_gitignore,
    main_py,
    makefile,
    pyproject_toml,
    readme_md,
    test_main_py,
    vscode_settings_json,
)

TERM_COL_CYAN = "\033[36m"
TERM_COL_LIGHT_GREEN = "\033[92m"
TERM_COL_RED = "\033[91m"
TERM_COL_RESET = "\033[0m"


def create_init_file(directory: str) -> None:
    create_file(directory, "__init__.py", "")


def create_file(directory: str, path: str, content: str) -> None:
    os.makedirs(directory, exist_ok=True)
    with open(path_join(directory, path), "xt", encoding="utf-8") as file:
        file.write(content)


def run_command(directory: str, command: tuple[str, ...]) -> tuple[int, str, str]:
    my_env = dict(os.environ, POETRY_VIRTUALENVS_IN_PROJECT="true")
    with Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory, env=my_env) as process:
        stdout, stderr = process.communicate()
        return (process.returncode, stdout.decode(), stderr.decode())


def install_poetry_deps(directory: str) -> None:
    poetry_add_deps(directory, ["ruff", "mypy", "pylint"], group="dev")
    poetry_add_deps(directory, ["pytest", "coverage"], group="test")


def poetry_add_deps(directory: str, dependencies: list[str], group: str | None = None) -> None:
    group_args = ["--group", group] if group else []
    run_command(directory, tuple(["poetry", "add", *dependencies, *group_args]))


def get_git_username() -> str:
    author = ""
    ret, stdout, _ = run_command(os.getcwd(), ("git", "config", "--get", "user.name"))
    if ret == 0:
        author = stdout.strip()
        ret, stdout, _ = run_command(os.getcwd(), ("git", "config", "--get", "user.email"))
        if ret == 0:
            author += f" <{stdout.strip()}>"
    return author


def get_user_prompts(project_dir: str) -> dict[str, Any]:
    config: dict[str, Any] = {}
    prompts: list[tuple[str, type[str] | type[int], Any]] = [
        ("Package Name", str, project_dir),
        ("Version", str, "0.0.1"),
        ("Description", str, ""),
        ("license", str, ""),
        ("Author", str, get_git_username()),
        ("Line Length", int, 120),
    ]
    for desc, data_type, default in prompts:
        key = desc.lower().replace(" ", "_")
        while True:
            try:
                user_value = input(
                    f"{TERM_COL_CYAN}{desc} [{TERM_COL_LIGHT_GREEN}{default}{TERM_COL_CYAN}]: {TERM_COL_RESET}"
                )
                config[key] = data_type(user_value) if user_value else default
                break
            except ValueError:
                ...
    return config


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="Typy: Python project templating",
        description="Automatically create templated Python program using command-line wizzard.",
    )
    parser.add_argument("project_dir")
    cmd_args = vars(parser.parse_args())
    base_dir = path_join(os.getcwd(), cmd_args["project_dir"])

    if os.path.isdir(base_dir):
        print(f"\n{TERM_COL_RED}x Directory already exists")
        return 1

    config = get_user_prompts(cmd_args["project_dir"])
    config["python_version"] = f"{sys.version_info.major}.{sys.version_info.minor}"

    print("\nCreating files...")

    # root dir
    create_file(base_dir, "pyproject.toml", pyproject_toml.format_file(**config))
    create_file(base_dir, "Makefile", makefile.format_file(**config))
    create_file(base_dir, "README.md", readme_md.format_file(**config))
    create_file(base_dir, ".gitignore", dot_gitignore.format_file())

    # /.vscode dir
    vscode_dir = path_join(base_dir, ".vscode")
    create_file(vscode_dir, "settings.json", vscode_settings_json.format_file(**config))

    # {package} di
    project_dir = path_join(base_dir, config["package_name"])
    create_init_file(project_dir)
    create_file(project_dir, "main.py", main_py.format_file())

    # tests dir
    tests_dir = path_join(base_dir, "tests")
    init_py_content = 'import pytest\n\npytest.register_assert_rewrite("conftest")\n'
    create_file(tests_dir, "__init__.py", init_py_content)
    create_file(tests_dir, "conftest.py", "")
    create_file(tests_dir, "test_main.py", test_main_py.format_file(**config))

    print("\nInstalling core dependencies...")
    install_poetry_deps(base_dir)

    print(f"\n{TERM_COL_LIGHT_GREEN}✓ All done!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
