from src.iso8583.bits import BitMap, BitMapType

from pytest_bdd import parsers, scenario, given, when, then

FEATURE_FILE = '../features/Bitmap.feature'


@scenario(FEATURE_FILE, 'Parse - Field 1')
def test_parse_field_1():
    pass


@scenario(FEATURE_FILE, 'Parse - Field 2')
def test_parse_field_2():
    pass


@scenario(FEATURE_FILE, 'Wikipedia Example')
def test_wikipedia_example():
    pass


@given(parsers.parse('a hexadecimal bitmap value of {bitmap_value}'))
def hexadecimal_bitmap_value(bitmap_value: str, context):
    context['bitmap_type'] = BitMapType.Hexadecimal
    context['bitmap_value'] = bitmap_value


@given(parsers.parse('a binary bitmap value of {bitmap_value}'))
def binary_bitmap_value(bitmap_value: str, context):
    context['bitmap_type'] = BitMapType.Binary
    context['bitmap_value'] = bitmap_value


@when('I parse the bitmap')
def parse_bitmap(context):
    try:
        context['result'] = BitMap.parse(context['bitmap_value'], context['bitmap_type'])
    except Exception as err:
        context['errors'].append(err)


@then(parsers.parse('field {field_number:d} should be present'))
def field_present(field_number: int, context):
    assert field_number in context['result']


@then(parsers.parse('all fields other than {field_number:d} should be absent'))
def all_fields_absent(field_number: int, context):
    for i in range(1, 65):
        if i != field_number:
            assert i not in context['result']


@then(parsers.parse('fields {field_numbers} should be present'))
def fields_present(field_numbers: str, context):
    fields_present = context.get('result', [])

    for field_number in field_numbers.split(','):
        field_number = field_number.strip()
        field_number = int(field_number)

        assert field_number in fields_present


@then(parsers.parse('fields other than {field_numbers} should be absent'))
def fields_absent(field_numbers: str, context):
    fields_present = context.get('result', [])

    for field_number in range(1, 65):
        if field_number in fields_present:
            continue

        assert field_number not in fields_present
