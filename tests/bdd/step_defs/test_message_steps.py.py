from pytest_bdd import parsers, scenario, given, when, then

FEATURE_FILE = '../features/Message.feature'


@scenario(FEATURE_FILE, 'Network Management Message')
def test_example_iso_network_management_message():
    pass


@scenario(FEATURE_FILE, 'Network Management Message Response')
def test_example_iso_network_management_message_response():
    pass


@given(parsers.parse('a hexadecimal message {hex_message}'))
def hexadecimal_message(hex_message: str, context):
    raise NotImplementedError(
        u'STEP: Given a hexadecimal message 0800823A0000000000000400000000000000042009061390000109061304200420001')


@when('I parse the message')
def parse_message():
    raise NotImplementedError(u'STEP: When I parse the message')


@then(parsers.parse('the message type indicator should be {expected_message_type_indicator}'))
def message_type_indicator_validation(expected_message_type_indicator: str):
    raise NotImplementedError(u'STEP: And the message type indicator should be 0800')


@then(parsers.parse('the message version should be {expected_version}'))
def message_version(expected_version: str):
    raise NotImplementedError(u'STEP: And the message version should be 1987')


@then(parsers.parse('the message class should be {expected_message_class}'))
def message_class(expected_message_class: str):
    raise NotImplementedError(u'STEP: And the message class should be Network Management')


@then(parsers.parse('the message function should be {expected_message_function}'))
def message_function(expected_message_function: str):
    raise NotImplementedError(u'STEP: And the message function should be Request')


@then(parsers.parse('the message origin should be {expected_message_origin}'))
def message_origin():
    raise NotImplementedError(u'STEP: And the message origin should be Acquirer')


@then(parsers.parse('the primary bitmap should be {expected_primary_bitmap}'))
def primary_bitmap(expected_primary_bitmap: str):
    raise NotImplementedError(u'STEP: And the primary bitmap should be 823A000000000000')


@then(parsers.parse('the secondary bitmap should be {expected_secondary_bitmap}'))
def secondary_bitmap(expected_secondary_bitmap: str):
    raise NotImplementedError(u'STEP: And the secondary bitmap should be 0400000000000000')


@then('the secondary bitmap should not be present')
def secondary_bitmap_not_present():
    raise NotImplementedError(u'STEP: And the secondary bitmap should not be present')


@then(parsers.parse('the transmission date and time should be {expected_transmission_date_and_time}'))
def transmission_date_and_time(expected_transmission_date_and_time: str):
    raise NotImplementedError(u'STEP: And the transmission date and time should be 0420090613')


@then(parsers.parse('the system trace audit number should be {expected_system_trace_audit_number}'))
def system_trace_audit_number(expected_system_trace_audit_number: str):
    raise NotImplementedError(u'STEP: And the system trace audit number should be 900001')


@then(parsers.parse('the local transaction time should be {expected_local_transaction_time}'))
def local_transaction_time(expected_local_transaction_time: str):
    raise NotImplementedError(u'STEP: And the local transaction time should be 090613')


@then(parsers.parse('the local transaction date should be {expected_local_transaction_date}'))
def local_transaction_date(expected_local_transaction_date: str):
    raise NotImplementedError(u'STEP: And the local transaction date should be 0420')


@then(parsers.parse('the settlement date should be {expected_settlement_date}'))
def settlement_date(expected_settlement_date: str):
    raise NotImplementedError(u'STEP: And the settlement date should be 0420')


@then(parsers.parse('the network management information code should be {expected_network_management_information_code}'))
def network_management_code():
    raise NotImplementedError(u'STEP: And the network management information code should be 0001')


@then(parsers.parse('the response code should be {expected_response_code}'))
def response_code():
    raise NotImplementedError(u'STEP: And the response code should be 00')


@then(parsers.parse('the action date should be {expected_action_date}'))
def action_date():
    raise NotImplementedError(u'STEP: And the action date should be 0420')
