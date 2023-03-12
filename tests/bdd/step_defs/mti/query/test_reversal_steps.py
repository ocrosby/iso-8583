from pytest_bdd import when, scenario

FEATURE_FILE = '../../../features/mti/query/Reversal.feature'


@scenario(FEATURE_FILE, 'Reversal Query None')
def test_reversal_query_none():
    pass


@scenario(FEATURE_FILE, 'Reversal Query x0x0')
def test_reversal_query_x0x0():
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


@when('I determine if the message type indicator is a reversal')
def mti_is_reversal(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', message_type_indicator.is_reversal())
    except Exception as err:
        errors.append(err)
