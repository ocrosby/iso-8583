from pytest_bdd import when, scenario

FEATURE_FILE = '../../features/mti/Function.feature'


@scenario(FEATURE_FILE, 'Function xx0x')
def test_function_xx0x():
    pass


@scenario(FEATURE_FILE, 'Function xx1x')
def test_function_xx1x():
    pass


@scenario(FEATURE_FILE, 'Function xx2x')
def test_function_xx2x():
    pass


@scenario(FEATURE_FILE, 'Function xx3x')
def test_function_xx3x():
    pass


@scenario(FEATURE_FILE, 'Function xx4x')
def test_function_xx4x():
    pass


@scenario(FEATURE_FILE, 'Function xx5x')
def test_function_xx5x():
    pass


@scenario(FEATURE_FILE, 'Function xx6x')
def test_function_xx6x():
    pass


@scenario(FEATURE_FILE, 'Function xx7x')
def test_function_xx7x():
    pass


@scenario(FEATURE_FILE, 'Function xx8x')
def test_function_xx8x():
    pass


@scenario(FEATURE_FILE, 'Function xx9x')
def test_function_xx9x():
    pass


@scenario(FEATURE_FILE, 'Function xxZx')
def test_function_xxzx():
    pass


@when('I determine the indicators function')
def mti_function(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', str(message_type_indicator.function))
    except Exception as err:
        errors.append(err)
