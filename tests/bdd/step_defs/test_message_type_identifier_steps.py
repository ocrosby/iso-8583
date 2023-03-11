from src.iso8583.mti import MessageTypeIndicator

from pytest_bdd import scenario, given, when, parsers

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
def test_version_zxxx():
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


@scenario(FEATURE_FILE, 'Reversal Query x4x0')
def test_reversal_query_x4x0():
    pass


@scenario(FEATURE_FILE, 'Reversal Query x4x1')
def test_reversal_query_x4x1():
    pass


@scenario(FEATURE_FILE, 'Reversal Query x4x2')
def test_reversal_query_x4x2():
    pass


@scenario(FEATURE_FILE, 'Reversal Query x4x3')
def test_reversal_query_x4x3():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query x4x0')
def test_chargeback_query_x4x0():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query x4x1')
def test_chargeback_query_x4x1():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query x4x2')
def test_chargeback_query_x4x2():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query x4x3')
def test_chargeback_query_x4x3():
    pass


@scenario(FEATURE_FILE, 'Reversal Query x0x0')
def test_reversal_query_x0x0():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query x0x0')
def test_chargeback_query_x0x0():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query None')
def test_chargeback_query_none():
    pass


@scenario(FEATURE_FILE, 'Reversal Query None')
def test_reversal_query_none():
    pass


@given(parsers.parse('a message type indicator {value}'))
def mti_setup(value: str, context):
    mti = MessageTypeIndicator(value)
    context.setdefault('message_type_indicator', mti)


@given('an undefined message type indicator')
def mti_setup_undefined(context):
    mti = MessageTypeIndicator(None)
    context.setdefault('message_type_indicator', mti)



@when("I determine the indicators version")
def mti_version(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', str(message_type_indicator.version))
    except Exception as err:
        errors.append(err)


@when('I determine the indicators purpose')
def mti_purpose(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', str(message_type_indicator.purpose))
    except Exception as err:
        errors.append(err)


@when('I determine if the message type indicator is a reversal')
def mti_is_reversal(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', message_type_indicator.is_reversal())
    except Exception as err:
        errors.append(err)


@when('I determine if the message type indicator is a chargeback')
def mti_is_chargeback(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', message_type_indicator.is_chargeback())
    except Exception as err:
        errors.append(err)
