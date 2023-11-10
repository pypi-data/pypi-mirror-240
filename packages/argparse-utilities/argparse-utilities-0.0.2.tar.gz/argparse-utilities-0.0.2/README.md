# argparse-utilities

*Actions and other utility functions for use with argparse*

## Quickstart

Install from pip:

```shell
pip install argparse-utilities
```

## Usage

```python
import argparse
from argparse_utilities import StoreMaxOneAction

parser = argparse.ArgumentParser(
    prog='Foo',
    description='foo foo foo',
)

parser.add_argument(
    '-f', '--foo',
    action=StoreMaxOneAction,
    type=int,
    required=True,
)

x = parser.parse_args(['--foo', '1'])
# x will be argparse.Namespace(foo=1)

parser.parse_args(['--foo', '1', '--foo', '2'])
# will throw ValueError('--foo supplied more than once')
```


## Development

For those developing or maintaining the `argparse-utilities` package itself,
be sure to install it with the `[dev]` option to pull in packages
used when developing.

    pip install --editable .[dev]

When developing, this package uses `pre-commit`.  After the initial
clone of the repository, you will need to set up pre-commit with:

    # in the top level of the checked-out repository:
    pre-commit install

## Changelog

### 0.0.2 released 2023-11-09
* Initial Version
