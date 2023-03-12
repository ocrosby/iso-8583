from pytest_bdd import when, scenario

FEATURE_FILE = '../../features/mti/Origin.feature'


@scenario(FEATURE_FILE, 'Origin - Acquirer')
def test_origin_acquirer():
    pass


@scenario(FEATURE_FILE, 'Origin - Acquirer Repeat')
def test_origin_acquirer_repeat():
    pass


@scenario(FEATURE_FILE, 'Origin - Issuer')
def test_origin_issuer():
    pass


@scenario(FEATURE_FILE, 'Origin - Issuer Repeat')
def test_origin_issuer_repeat():
    pass


@scenario(FEATURE_FILE, 'Origin - Other')
def test_origin_other():
    pass


@scenario(FEATURE_FILE, 'Origin - Reserved by ISO 6')
def test_origin_reserved_by_iso_6():
    pass


@scenario(FEATURE_FILE, 'Origin - Invalid')
def test_origin_invalid():
    pass


@when('I determine the indicators origin')
def mti_origin(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        origin = message_type_indicator.origin
        context.setdefault('result', str(origin))
    except Exception as e:
        errors.append(e)
