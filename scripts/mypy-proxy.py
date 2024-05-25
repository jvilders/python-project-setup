import subprocess
import sys


def get_venv_subdirectory(platform: str) -> str:
    """Get the venv subdirectory for the current operating system.

    Pre-commit runs mypy (like all hooks) in a separate virtual environment. By default when
    pre-commit runs mypy, it uses the global python executable outside the project virtual
    environment, which does not have the package dependencies installed. Mypy is then unable
    to check types of imports. By providing the path to the executable of the virtual
    environment, the installed packages are 'seen' by mypy.

    On Windows: .venv/Scripts/python
    On any other OS: .venv/bin/python
    Done by convention >15 years ago: https://github.com/pypa/virtualenv/commit/993ba1316a83b760370f5a3872b3f5ef4dd904c1.
    """
    if platform == "win32":
        return "Scripts"
    return "bin"


if __name__ == "__main__":
    python_executable_location = f".venv/{get_venv_subdirectory(sys.platform)}/python"

    result = subprocess.run(
        ["mypy", ".", "--python-executable", python_executable_location],
    )

    sys.exit(result.returncode)
