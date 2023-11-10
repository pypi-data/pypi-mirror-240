import argparse

import pytest
from argparse_utilities import StoreMaxOneAction


@pytest.fixture
def parser_foo():
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
    return parser


def test_store_max_one_action_pass(parser_foo) -> None:
    x = parser_foo.parse_args(['--foo', '1'])
    assert x == argparse.Namespace(foo=1)


def test_store_max_one_action_fail(parser_foo) -> None:
    with pytest.raises(ValueError, match='--foo supplied more than once'):
        parser_foo.parse_args(['--foo', '1', '--foo', '2'])
