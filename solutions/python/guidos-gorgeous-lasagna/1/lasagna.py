"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Return the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Return the preparation time based on the number of layers.

    Each layer takes 2 minutes to prepare.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes).
    """
    return layers * 2


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Return the total elapsed cooking time.

    It is the sum of the preparation time and the baking time already elapsed.

    :param layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time spent (in minutes).
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time