"""Contains tests for src.mutual_elements.get_mutual_elements function"""

from typing import Any

import pytest

from src.mutual_elements import get_mutual_elements


@pytest.mark.parametrize(
    "first_list,second_list,expected_elements",
    [
        (["a", "b", "c"], ["c", "d", "e"], ["c"]),
        (["a", "b", "c"], ["c", "c", "e"], ["c"]),
        (["a", "c", "c"], ["c", "d", "e"], ["c"]),
        (["a", "b", "c"], ["d", "e", "f"], []),
        ([1, 2, 3], [3, 4, 5], [3]),
        ([1, 2, 3], [3, 3, 5], [3]),
        ([1, 3, 3], [3, 4, 5], [3]),
        ([1, 2, 3], [4, 5, 6], []),
        ([1.4, 2.5, 3.6], [3.6, 4.7, 5.8], [3.6]),
        ([1.4, 2.5, 3.6], [3.6, 3.6, 5.8], [3.6]),
        ([1.4, 3.6, 3.6], [3.6, 4.7, 5.8], [3.6]),
        ([1.4, 2.5, 3.6], [4.7, 5.8, 6.9], []),
        ([(1, 2,), (3, 4,), (5, 6,)], [(5, 6,), (7, 8,), (9, 10,)], [(5, 6,)]),
        ([(1, 2,), (3, 4,), (5, 6,)], [(5, 6,), (5, 6,), (9, 10,)], [(5, 6,)]),
        ([(1, 2,), (5, 6,), (5, 6,)], [(5, 6,), (7, 8,), (9, 10,)], [(5, 6,)]),
        ([(1, 2,), (3, 4,), (5, 6,)], [(7, 8,), (9, 10,), (11, 12,)], []),
        ([[1, 2], [3, 4], [5, 6]], [[5, 6], [7, 8], [9, 10]], [[5, 6]]),
        ([[1, 2], [3, 4], [5, 6]], [[5, 6], [5, 6], [9, 10]], [[5, 6]]),
        ([[1, 2], [5, 6], [5, 6]], [[5, 6], [7, 8], [9, 10]], [[5, 6]]),
        ([[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], []),
        ([{"a": 1}, {"b": 2}], [{"b": 2}, {"c": 3}], [{"b": 2}]),
        ([{"a": 1}, {"b": 2}], [{"b": 2}, {"b": 2}], [{"b": 2}]),
        ([{"b": 2}, {"b": 2}], [{"b": 2}, {"c": 3}], [{"b": 2}]),
        ([{"a": 1}, {"b": 2}], [{"b": 1}, {"c": 3}], []),
    ]
)
def test_mutual_elements(
    first_list: list[Any],
    second_list: list[Any],
    expected_elements: list[Any],
) -> None:
    """Tests get_mutual_elements function.

    Args:
        first_list (list[Any]): The first list of elements to compare.
        second_list (list[Any]): The second list of elements to compare.
        expected_elements (list[Any]): The expected list of mutual elements found in both lists.
    """
    elements = get_mutual_elements(
        first_list=first_list,
        second_list=second_list,
    )
    assert elements == expected_elements
