# rgprc

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A simple to use, reflection only - grpc client.

## Features

- Make GRPC calls against reflection enabled servers

## How to install

``` shell
pip install rgrpc
```

## How to use

``` python
try:
    rgrpc_client = Client('localhost:50051')
    response = rgprc_client.request('myserver.myservice', 'mymethod', {'field1':'value1'})
except Exception as e:
    logger.error(f"Failed to initialize rgrpc client: {e}")
```

## Developer Setup

### Environment Setup

1. `python3 -m venv /where/you/like/to/store/venvs`
2. `source /venv/bin/activate`
3. `pip install -r dev-requirements.txt`
4. `pre-commit install`

### Running tests

Running `tests.sh` will execute the following actions:

- `ruff check ./rgrpc` - will run the [ruff](https://docs.astral.sh/ruff/linter/) linter over core source files
- `ruff format ./rgrpc` - will run the [ruff](https://docs.astral.sh/ruff/formatter/) formatter over core source files
- `mypy rgprc/*.py` - will run [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) over core source files.
- `pytest --cov=rgrpc tests/` - will run tests and generate a short coverage report

## Maintainers

- [ViridianForge](viridianforge.tech)
