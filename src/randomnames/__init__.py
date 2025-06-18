"""This is the main entry point for the package."""

import random

from .animals import ANIMALS
from .adjectives import ADJECTIVES


def create_name(sep: str = "-") -> str:
    """Create a random name with a separator.

    Parameters
    ----------
    sep : str, optional
        The separator to use between the random words, by default "-".

    """
    adj = random.choice(ADJECTIVES)
    animal = random.choice(ANIMALS)
    return f"{adj}{sep}{animal}"
