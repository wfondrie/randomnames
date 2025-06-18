"""Test that our package is actually working."""

import pytest
import randomnames


def test_create_default_name():
    """Test that the names are what we expect."""
    name = randomnames.create_name()
    assert isinstance(name, str)
    assert "-" in name
    adj, animal = name.split("-")
    assert adj in randomnames.ADJECTIVES
    assert animal in randomnames.ANIMALS


@pytest.mark.parametrize("sep", ["_", " ", ".", 1])
def test_create_custom_separator(sep):
    """Test that we can create a name with a custom separator."""
    name = randomnames.create_name(sep=sep)
    assert isinstance(name, str)
    assert str(sep) in name
    adj, animal = name.split(str(sep))
    assert adj in randomnames.ADJECTIVES
    assert animal in randomnames.ANIMALS
    raise ValueError("Fake error")
