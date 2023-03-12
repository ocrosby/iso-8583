import pytest

from typing import Dict, List

from pytest_bdd import parsers, given, then

from tests.tools.src import conversion

# Global Fixtures


@pytest.fixture
def errors() -> List[Exception]:
    return []


@pytest.fixture
def context() -> Dict[str, any]:
    return {}


# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    errors = request.getfixturevalue('errors')
    errors.append(exception)

    print(f'Step failed: "{step}"')


def pytest_bdd_apply_tag(tag, function):
    if tag == 'todo':
        marker = pytest.mark.skip(reason='Not implemented yet')
        marker(function)
        return True
    elif tag == 'skip':
        marker = pytest.mark.skip(reason='Skipped')
        marker(function)
        return True
    elif tag == 'ignore':
        marker = pytest.mark.skip(reason='Ignored')
        marker(function)
        return True
    else:
        # Fall back to the default behavior of pytest-bdd
        return None


# When Steps


@given('an empty binary string')
def empty_binary_string(context):
    context['binary_string'] = ''


@then("there should be no errors")
def no_errors(errors):
    assert len(errors) == 0


@then(parsers.parse('the result should be {expected_value}'))
def validate_result(expected_value: any, context):
    if conversion.is_boolean_string(expected_value):
        expected_value = conversion.string_to_boolean(expected_value)

    if expected_value == 'empty':
        result = context.get('result')
        length = len(result)

        assert length == 0
    else:
        assert expected_value == context.get('result')


@then(parsers.parse('the result should be {expected_value} in hexadecimal'))
def validate_result_hex(expected_value: str, context):
    expected_value = expected_value.replace(' ', '')
    expected_bytearray = bytearray.fromhex(expected_value)

    actual_bytearray = context.get('byte_array')

    assert expected_bytearray == actual_bytearray


@then(parsers.parse('the result should be {expected_value} in binary'))
def validate_result_binary(expected_value: str, context):
    assert bin(int(expected_value)) == context.get('result')


@then(parsers.parse('there should be an error containing {expected_substring}'))
def validate_error(expected_substring: str, errors):
    assert len(errors) > 0

    found = False
    for error in errors:
        if expected_substring in str(error):
            found = True
            break

    assert found
