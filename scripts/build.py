"""Builds the library wheel and tarball, with stubs included.

Core concept is:
- Make a copy of the package folder.
- Generate stub files
- Add marker file as per PEP-561 to indicate package can be type-checked

Notes:
- the `poetry publish` command by default uses the folder with the same name
as the project. To both be able to work with this command but also not add
stub files (and the marker file) to this original folder (leaving the package
folder in the same state as before running the build script), some additional
steps are used.
"""

import os
import shutil
import subprocess
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from pathlib import Path


def get_package_name() -> str:
    pyproject_toml_file = Path(__file__).parent.parent.joinpath("pyproject.toml")

    with open(pyproject_toml_file, "rb") as f:
        data = tomllib.load(f)
        package_name: str = data["tool"]["poetry"]["name"]
        return package_name


if __name__ == "__main__":
    PACKAGE_NAME = get_package_name()
    print(f"Package name is {PACKAGE_NAME}")

    # Build stubs in intermediate folder
    subprocess.run(["stubgen", f"./{PACKAGE_NAME}/"])

    # Copy package files to intermediate folder
    shutil.copytree(PACKAGE_NAME, f"out/{PACKAGE_NAME}", dirs_exist_ok=True)

    # Add py.typed marker file
    open(f"out/{PACKAGE_NAME}/py.typed", "a").close()

    # Rename original package folder to temporary folder
    os.rename(PACKAGE_NAME, "temporary")

    # Put intermediate folder in root, to prepare for publishing
    os.rename(f"out/{PACKAGE_NAME}", PACKAGE_NAME)

    # Build the package using poetry"
    subprocess.run(["poetry", "build"])

    # Clean up intermediate folders
    shutil.rmtree("out")
    shutil.rmtree(PACKAGE_NAME)

    # Put original package folder back
    os.rename("temporary", PACKAGE_NAME)
