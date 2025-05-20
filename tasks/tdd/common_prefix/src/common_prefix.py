"""Contains functions for obtaining common prefixes for URLs"""

from typing import Any


def is_list_of_strings(
    lst: Any,
) -> bool:
    """Checks if the provided object is a list where all elements are strings.

    Args:
        lst (Any): The object to check.

    Returns:
        bool: True if lst is a list and all its elements are strings, False otherwise.
    """
    if isinstance(lst, list):
        return all(isinstance(element, str) for element in lst)
    return False


def get_common_prefix(
    urls: list[str],
) -> str:
    """Finds the longest common prefix string among a list of URLs.

    Args:
        urls (list[str]): A list of strings representing URLs.

    Returns:
        str: The longest common prefix shared by all URLs in the list.
            Returns an empty string if the list is empty or if there is no common prefix.

    Raises:
        ValueError: If 'urls' is not a list of strings.
    """
    if not is_list_of_strings(urls):
        raise ValueError("'urls' argument must be a list of strings")
    if not urls:
        return ""
    common_prefix = urls[0]
    for url in urls[1:]:
        for i, symbol in enumerate(common_prefix):
            if symbol != url[i]:
                common_prefix = common_prefix[:i]
                break
        if common_prefix == "":
            return ""
    return common_prefix
