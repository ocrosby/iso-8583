from pytest_bdd import when, scenario

FEATURE_FILE = '../../features/mti/Purpose.feature'


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


@when('I determine the indicators purpose')
def mti_purpose(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', str(message_type_indicator.purpose))
    except Exception as err:
        errors.append(err)
