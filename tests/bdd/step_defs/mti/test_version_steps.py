from pytest_bdd import scenario, when

FEATURE_FILE = '../../features/mti/Version.feature'


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


@when("I determine the indicators version")
def mti_version(context, errors):
    try:
        message_type_indicator = context['message_type_indicator']
        context.setdefault('result', str(message_type_indicator.version))
    except Exception as err:
        errors.append(err)
