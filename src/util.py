#!/usr/bin/env python3.12

import re

def is_plain_object(obj) -> bool:
    """
    Check if a value is a plain object (an object that is not an list).

    Args:
        obj: The value to check.

    Returns:
        bool: True if the value is a plain object, False otherwise.
    """
    return obj is not None and isinstance(obj, dict)


def is_valid_version_number(ver):
    """ 
    Check if a version number string is valid.
    :param ver: The version text to check.
    """
    if ver and isinstance(ver, str) and re.compile(r'^v\d+(\.\d+)+$').fullmatch(ver): 
        return True
    else: 
        return False

def is_valid_index(index: str | int) -> bool:
    """
    Checks if an index value is valid.

    Args:
        index (str | int): The index value to check.

    Returns:
        bool: True if the index is valid, False otherwise.
    """
    try:
        index_int = int(index)
        return isinstance(index_int, int)
    except (ValueError, TypeError):
        return False