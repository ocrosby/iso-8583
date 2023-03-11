from src.iso8583 import mti

from pytest_bdd import scenario, given, when, then, parsers

FEATURE_FILE = '../features/MessageTypeIndicator.feature'


@scenario(FEATURE_FILE, 'Version 0xxx')
def test_version_0xxx():
    pass


@scenario(FEATURE_FILE, 'Version 1xxx')
def test_version_1xxx():
    pass


@scenario(FEATURE_FILE, 'Version 2xxx')
def test_version_2xxx():
    pass


@scenario(FEATURE_FILE, 'Version 3xxx')
def test_version_3xxx():
    pass


@scenario(FEATURE_FILE, 'Version 4xxx')
def test_version_4xxx():
    pass


@scenario(FEATURE_FILE, 'Version 5xxx')
def test_version_5xxx():
    pass


@scenario(FEATURE_FILE, 'Version 6xxx')
def test_version_6xxx():
    pass


@scenario(FEATURE_FILE, 'Version 7xxx')
def test_version_7xxx():
    pass


@scenario(FEATURE_FILE, 'Version 8xxx')
def test_version_8xxx():
    pass


@scenario(FEATURE_FILE, 'Version 9xxx')
def test_version_9xxx():
    pass


@scenario(FEATURE_FILE, 'Version Zxxx')
def test_version_Zxxx():
    pass


@scenario(FEATURE_FILE, 'Purpose x0xx')
def test_purpose_x0xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x1xx')
def test_purpose_x1xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x2xx')
def test_purpose_x2xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x3xx')
def test_purpose_x3xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x4xx')
def test_purpose_x4xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x5xx')
def test_purpose_x5xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x6xx')
def test_purpose_x6xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x7xx')
def test_purpose_x7xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x8xx')
def test_purpose_x8xx():
    pass


@scenario(FEATURE_FILE, 'Purpose x9xx')
def test_purpose_x9xx():
    pass


@scenario(FEATURE_FILE, 'Purpose xZxx')
def test_purpose_xzxx():
    pass


@given(parsers.parse('a message type indicator {message_type_indicator:S}'))
def mti_setup(message_type_indicator: str, context):
    context.setdefault('message_type_indicator', message_type_indicator)


@when("I determine the indicators version")
def mti_version(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        meaning = mti.version(message_type_indicator)
        context.setdefault('result', str(meaning))
    except Exception as err:
        errors.append(err)


@when('I determine the indicators purpose')
def mti_purpose(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        meaning = mti.purpose(message_type_indicator)

        context.setdefault('result', str(meaning))
    except Exception as err:
        errors.append(err)