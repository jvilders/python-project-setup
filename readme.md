# Prerequisites

Requires `poetry`, but `pyenv` is also recommended.

## Windows
### `pyenv-win`
- Go to [the GitHub repo](https://github.com/pyenv-win/pyenv-win)
- follow the quick start instructions (if needed, change powershell executionPolicy to RemoteSigned so you can run the install script)
- install a python version using `pyenv install [version here]`
- set that python version as the global version by using `pyenv global` (you can always change it later)

### `poetry`
#### Prerequisites

Poetry's [recommended install instructions](https://python-poetry.org/docs/#installation) use `pipx`. The [install instructions](https://github.com/pypa/pipx) for `pipx` on Windows recommend using `scoop`.

1. Installing `scoop`
    - install scoop using the powershell command provided on [its site](https://scoop.sh/)
2. Installing `pipx`
    - run the commands mentioned in the `pipx` install instructions

#### Installing poetry

- run the commands mentioned in the `poetry` install instructions using pipx
- set these two poetry environment variables:
  - `virtualenvs.in-project`: Install dependencies in a folder inside the project. Run: 
      
      `poetry config virtualenvs.in-project true`

  - `virtualenvs.prefer-active-python`: Use currently activated python version to create new virtual environments (pyenv). Run:
  
     `poetry config virtualenvs.prefer-active-python true`

## Mac

(Install instructions for pyenv and poetry here)

# Installation

- Use the python version specified in the `.python-version` file with `pyenv`
- Run `poetry install --sync`
- Activate the poetry environment by running `poetry shell`
- If applicable, point your IDE towards the python interpreter inside the virtual environment, so that it can use the installed packages for type checking
- Run `pre-commit install --hook-type pre-commit --hook-type pre-push` to set up the pre-commit and pre-push hooks

# Commands

Poe the poet is used as a task runner. Some convenience commands are provided, run `poe` within the virtual environment to see configured tasks and their descriptions.

These commands are used in the pre-commit hooks, the idea being that these hooks will always use the exact same underlying package versions as when running these commands manually. 