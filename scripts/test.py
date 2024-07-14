"""Runs unit tests and prints coverage.

To get coverage, the package name must be specified. To avoid hardcoding this, this script is used
rather than defining a call to pytest directly in the pyproject.toml file as a poe task.
"""

import subprocess

from .utils import get_package_name

if __name__ == "__main__":
    package_name = get_package_name()
    subprocess.run(
        [
            "pytest",
            f"--cov={package_name}",
            "--cov-report",
            "term-missing",
            "--cov-report",
            "html",
            "tests/",
        ]
    )
