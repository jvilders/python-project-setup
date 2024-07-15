"""This script is used to publish the built package.

This provides a place to customize your publishing options,
such as to which repository (possibly private, make sure you've
authenticated in the pre-install script in that case) you will
publish.
"""

import subprocess

if __name__ == "__main__":
    subprocess.run(["poetry", "publish"])
