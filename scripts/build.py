"""Builds the library wheel and tarball."""

import subprocess

if __name__ == "__main__":
    # Build the package using poetry"
    subprocess.run("poetry build", shell=True, check=True)
