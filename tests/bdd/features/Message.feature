# Created by omarcrosby at 3/12/23
Feature: ISO 8583 Messages
  As a developer
  I want to be able to parse ISO 8583 messages
  So that I can use them in my application

  Scenario: Network Management Message
    Given a hexadecimal message 0800823A0000000000000400000000000000042009061390000109061304200420001
    When I parse the message
    Then there should be no errors
    And the message type indicator should be 0800
    And the message version should be 1987
    And the message class should be Network Management
    And the message function should be Request
    And the message origin should be Acquirer
    And the primary bitmap should be 823A000000000000
    And the secondary bitmap should be 0400000000000000
    And the transmission date and time should be 0420090613
    And the system trace audit number should be 900001
    And the local transaction time should be 090613
    And the local transaction date should be 0420
    And the settlement date should be 0420
    And the network management information code should be 0001


  Scenario: Network Management Message Response
    Given a hexadecimal message 0810823A000002000000048000000000000004200906139000010906130420042000001031128
    When I parse the message
    Then there should be no errors
    And the message type indicator should be 0810
    And the message version should be 1987
    And the message class should be Network Management
    And the message function should be Request Response
    And the message origin should be Acquirer
    And the primary bitmap should be 823A000002000000
    And the secondary bitmap should be 0480000000000000
    And the transmission date and time should be 0420090613
    And the system trace audit number should be 900001
    And the local transaction time should be 090613
    And the local transaction date should be 0420
    And the settlement date should be 0420
    And the response code should be 00
    And the network management information code should be 001
    And the action date should be 031128


  Scenario: Financial Transaction Message
    Given a hexadecimal message 0200323A40010841801038000000000000000004200508050113921208050420042251320720000010000001156040800411 01251146333156336000299
    When I parse the message
    Then there should be no errors
    And the message type indicator should be 0200
    And the message version should be 1987
    And the message class should be Financial Transaction
    And the message function should be Request
    And the message origin should be Acquirer
    And the primary bitmap should be 823A400108418010
    And the secondary bitmap should not be present
    And the processing code should be 380000
    And the amount, transaction should be 000000000000
    And the transmission date and time should be 0420050805
    And the system trace audit number should be 011392
    And the local transaction time should be 120805
    And the local transaction date should be 0420
    And the settlement date should be 0422
    And the merchant type, or category code should be 5132
    And the acquiring institution identification code should be 20 000
    And the retrieval reference number should be 010000001156
    And the card acceptor identification code should be 040800411 01251
    And the additional data should be 333156336000299
    And the currency code, transaction should be empty
