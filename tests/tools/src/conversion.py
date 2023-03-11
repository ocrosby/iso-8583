def is_boolean_string(string: str) -> bool:
    """Check if a string is a boolean."""

    if string in ['false', 'False', 'FALSE', 'true', 'True', 'TRUE']:
        return True

    return False


def string_to_boolean(string: str) -> bool:
    """Convert a string to a boolean."""

    if string in ['false', 'False', 'FALSE']:
        return False

    return True
