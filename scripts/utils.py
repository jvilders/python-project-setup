import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from pathlib import Path


def get_package_name() -> str:
    """Utility function to reads the root-level pyproject.toml file and return the project name."""
    pyproject_toml_file = Path(__file__).parent.parent.joinpath("pyproject.toml")

    with open(pyproject_toml_file, "rb") as f:
        data = tomllib.load(f)
        package_name: str = data["tool"]["poetry"]["name"]
        return package_name
