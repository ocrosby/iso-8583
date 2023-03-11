import pytest

from typing import Dict, List

from pytest_bdd import parsers, then

from tests.tools.src import conversion


@pytest.fixture
def errors() -> List[Exception]:
    return []


@pytest.fixture
def context() -> Dict[str, any]:
    return {}


@then("there should be no errors")
def no_errors(errors):
    assert len(errors) == 0


@then(parsers.parse('the result should be {expected_value}'))
def validate_result(expected_value: any, context):
    if conversion.is_boolean_string(expected_value):
        expected_value = conversion.string_to_boolean(expected_value)
        
    assert expected_value == context.get('result')


@then(parsers.parse('there should be an error containing {expected_substring}'))
def validate_error(expected_substring: str, errors):
    assert len(errors) > 0

    found = False
    for error in errors:
        if expected_substring in str(error):
            found = True
            break

    assert found
