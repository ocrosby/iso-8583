# from src.iso8583.mti import MessageTypeIndicator

from pytest_bdd import scenario, when, parsers

from tests.tools.src import conversion

FEATURE_FILE = '../features/BinaryData.feature'


@scenario(FEATURE_FILE, 'Byte Array Creation')
def test_byte_array_creation():
    pass


@scenario(FEATURE_FILE, 'Binary String Normalization Empty')
def test_binary_string_normalization_empty():
    pass


@when('I normalize the binary string')
def normalize_binary_string(context):
    try:
        context['result'] = conversion.normalize_binary_string(context['binary_string'])
    except Exception as err:
        context['errors'].append(err)

@when(parsers.parse('I create an array of {count:d} bytes'))
def byte_array_entry(count: int, context):
    try:
        context['byte_array'] = bytearray(count)
    except Exception as err:
        context['errors'].append(err)
