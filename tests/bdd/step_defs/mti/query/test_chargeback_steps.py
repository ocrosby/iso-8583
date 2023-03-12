from pytest_bdd import when, scenario

FEATURE_FILE = '../../../features/mti/query/Chargeback.feature'


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


@scenario(FEATURE_FILE, 'Chargeback Query x0x0')
def test_chargeback_query_x0x0():
    pass


@scenario(FEATURE_FILE, 'Chargeback Query None')
def test_chargeback_query_none():
    pass


@when('I determine if the message type indicator is a chargeback')
def mti_is_chargeback(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', message_type_indicator.is_chargeback())
    except Exception as err:
        errors.append(err)
