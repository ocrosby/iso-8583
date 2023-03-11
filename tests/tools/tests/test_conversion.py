from tests.tools.src.conversion import is_boolean_string, string_to_boolean


def test_is_boolean_string():
    """Test if a string is a boolean."""
    assert is_boolean_string('false')
    assert is_boolean_string('False')
    assert is_boolean_string('FALSE')
    assert is_boolean_string('true')
    assert is_boolean_string('True')
    assert is_boolean_string('TRUE')
    assert not is_boolean_string('foo')


def test_string_to_boolean():
    """Test converting a string to a boolean."""
    assert string_to_boolean('false') is False
    assert string_to_boolean('False') is False
    assert string_to_boolean('FALSE') is False
    assert string_to_boolean('true') is True
    assert string_to_boolean('True') is True
    assert string_to_boolean('TRUE') is True
    assert string_to_boolean('foo') is True
