def is_boolean_string(string: str) -> bool:
    """Check if a string is a boolean."""
    return string in ['false', 'False', 'FALSE', 'true', 'True', 'TRUE']


def string_to_boolean(string: str) -> bool:
    """Convert a string to a boolean."""
    return not string in ['false', 'False', 'FALSE']
