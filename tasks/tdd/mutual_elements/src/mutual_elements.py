"""Contains functions for getting unique mutual elements from two lists"""

from typing import Any


def get_mutual_elements(
    first_list: list[Any],
    second_list: list[Any],
) -> list[Any]:
    """Compares two lists and prepares a list of their unique mutual elements.

    Args:
        first_list (list[Any]): A list of arbitrary elements.
        second_list (list[Any]): A list of arbithrary elements.

    Returns:
        list[Any]: A list of unique mutual elements.
    """
    mutual_elements = []
    for element in first_list:
        if element in second_list and element not in mutual_elements:
            mutual_elements.append(element)
    return mutual_elements
