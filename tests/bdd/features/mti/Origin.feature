# Created by omarcrosby at 3/12/23
Feature: Message Type Indicator Origin
  As a developer
  I want to be able to determine the origin of the message type indicator
  So that I am aware of the location of the message source within the payment chain

  Scenario: Origin - Acquirer
    Given a message type indicator xxx0
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.Acquirer

  Scenario: Origin - Acquirer Repeat
    Given a message type indicator xxx1
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.AcquirerRepeat

  Scenario: Origin - Issuer
    Given a message type indicator xxx2
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.Issuer

  Scenario: Origin - Issuer Repeat
    Given a message type indicator xxx3
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.IssuerRepeat


  Scenario: Origin - Other
    Given a message type indicator xxx4
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.Other


  Scenario: Origin - Reserved by ISO 6
    Given a message type indicator xxx6
    When I determine the indicators origin
    Then there should be no errors
    And the result should be Origin.ReservedByIso
    
  Scenario: Origin - Invalid
    Given a message type indicator xxxZ
    When I determine the indicators origin
    Then there should be an error containing Invalid message type indicator    