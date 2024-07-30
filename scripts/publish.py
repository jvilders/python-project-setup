"""This script is used to publish the built package.

This provides a place to customize your publishing options,
such as to which repository you will publish. If private,
make sure to authenticate in the pre-install script.
"""

import subprocess

if __name__ == "__main__":
    subprocess.run("poetry publish --dry-run", shell=True, check=True)
