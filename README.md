# Prerequisites

This project requires [`poetry`](https://python-poetry.org/docs/#installation) and [`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).

## Poetry setup
Run the below commands to configure poetry. Note that these commands configure global poetry behavior, they do not have to be run in a specific location.

```bash
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true
```

The first option is set, because we prefer to keep dependencies inside of the project. This also keeps CI and local installs more similar.

The second instructs poetry to set up its virtual environment using the activated pyenv version and not your global python version, which helps prevent version mismatches.


# Installation

- Use the python version specified in the `.python-version` by running `pyenv local <that version>`. If you do not have this version, install it with pyenv first: `pyenv install <that version>`
- Run `poetry install --sync`
- Activate the poetry environment by running `poetry shell`
- If applicable, point your IDE towards the python interpreter inside the virtual environment, so that it can use the installed packages for auto-completion and type checking while developing
- Run `pre-commit install --hook-type pre-commit --hook-type pre-push` to set up the pre-commit and pre-push hooks

# Commands

Poe the poet is used as a task runner. Some convenience commands are provided, run `poe` within the virtual environment to see configured tasks and their descriptions.

These commands are also used in the pre-commit hooks, the idea being that these hooks will always use the exact same underlying package versions as when running these commands manually. 