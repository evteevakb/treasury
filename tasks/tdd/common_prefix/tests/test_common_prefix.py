"""Contains tests for src.common_prefix module"""

from typing import Any

import pytest

from src.common_prefix import get_common_prefix, is_list_of_strings


@pytest.mark.parametrize(
    "lst, expected_result",
    [
        ([], True),
        (["a", "b", "c"], True),
        ([1, 2, 3], False),
        (1, False),
    ],
)
def test_is_list_of_strings(
    lst: Any,
    expected_result: bool,
) -> None:
    """Tests the is_list_of_strings function.

    Args:
        lst (Any): The input to be checked.
        expected_result (bool): The expected boolean result indicating whether
            lst is a list of strings.
    """
    result = is_list_of_strings(lst)
    assert result == expected_result


class TestCommonPrefix:
    """Tests for get_common_prefix function"""

    @pytest.mark.parametrize(
        "urls,expected_common_prefix",
        [
            ([], ""),
            (["", ""], ""),
            (["", "abc"], ""),
            (["https://example.com"], "https://example.com"),
            (["https://a.com", "https://a.com"], "https://a.com"),
            (["abc", "antsd", "abfrt"], "a"),
            (["bc", "ntsd", "bfrt"], ""),
            (
                [
                    "http://www.google.com",
                    "http://www.google.api.com",
                    "http://www.google.abc.com",
                ],
                "http://www.google.",
            ),
            (["HTTPS://a.com", "https://a.com"], ""),
        ],
    )
    def test_success(
        self,
        urls: list[str],
        expected_common_prefix: str,
    ) -> None:
        """Tests that the get_common_prefix function returns the expected
            common prefix for a given list of URLs.

        Args:
            urls (list[str]): A list of URL strings to evaluate.
            expected_common_prefix (str): The expected common prefix string for the provided URLs.
        """
        common_prefix = get_common_prefix(urls)
        assert common_prefix == expected_common_prefix

    @pytest.mark.parametrize(
        "urls",
        [
            ([1, 2, 3]),
            (1),
        ],
    )
    def test_incorrect_values(
        self,
        urls: Any,
    ) -> None:
        """Tests that the get_common_prefix function raises a ValueError
            when provided with incorrect or invalid input values.

        Args:
            urls (Any): The invalid input values to be checked.
        """
        with pytest.raises(ValueError):
            get_common_prefix(urls)
