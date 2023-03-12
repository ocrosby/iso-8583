from pytest_bdd import given, parsers

from src.iso8583.mti import MessageTypeIndicator


@given(parsers.parse('a message type indicator {value}'))
def mti_setup(value: str, context):
    mti = MessageTypeIndicator(value)
    context.setdefault('message_type_indicator', mti)


@given('an undefined message type indicator')
def mti_setup_undefined(context):
    mti = MessageTypeIndicator(None)
    context.setdefault('message_type_indicator', mti)
