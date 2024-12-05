# Basic Python library setup
## Prerequisites

This project uses [`uv`](https://docs.astral.sh/uv/).

## Installation

- Use the python version specified in the `.python-version` by running `pyenv local <that version>`. If you do not have this version, install it with pyenv first: `pyenv install <that version>`
- Run `uv sync`. This will automatically use the python version from `.python-version`.
- If applicable, point your IDE towards the python interpreter inside the virtual environment, so that it can use the installed packages for auto-completion and type checking while developing
- Run `pre-commit install` to set up the pre-commit hooks

## Commands

Poe the poet is used as a task runner. Some convenience commands are provided, run `poe` within the virtual environment to see configured tasks and their descriptions.

These commands are also used in the pre-commit hooks, the idea being that these hooks will always use the exact same underlying package versions as when running these commands manually. 

## Workflows

This project comes with some basic Github Actions workflows just to give the idea of how it integrates with the project. It is not complete or production ready. Any production-ready library would need to tackel authentication for publishing, possibly pulling from and pushing to private registries, etc.