"""This script provides a place to run pre-install tasks.

This can be used for anything that seems suitable, but a common usecase is to
authenticate private repositories here. As this script is meant to be run prior
to project installation, third-party packages will not be available.

Ideally, the same script can be used in CI as well as locally. Credentials
should not be harcoded in this file, but (for example) provided as environment variables.
"""

if __name__ == "__main__":
    print("No pre-install setup necessary")
