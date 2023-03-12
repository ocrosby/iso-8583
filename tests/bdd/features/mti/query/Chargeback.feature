# Created by omarcrosby at 3/11/23
Feature: Chargeback Query
  As a developer
  I want to be able to determine if a message type indicator is a chargeback
  So that I can tell when the message charges back a previously cleared financial message

  Scenario: Chargeback Query x4x0
    Given a message type indicator x4x0
    When I determine if the message type indicator is a chargeback
    Then there should be no errors
    And the result should be false

  Scenario: Chargeback Query x4x1
    Given a message type indicator x4x1
    When I determine if the message type indicator is a chargeback
    Then there should be no errors
    And the result should be false

  Scenario: Chargeback Query x4x2
    Given a message type indicator x4x2
    When I determine if the message type indicator is a chargeback
    Then there should be no errors
    And the result should be true

  Scenario: Chargeback Query x4x3
    Given a message type indicator x4x3
    When I determine if the message type indicator is a chargeback
    Then there should be no errors
    And the result should be true

  Scenario: Chargeback Query x0x0
    Given a message type indicator x0x0
    When I determine if the message type indicator is a chargeback
    Then there should be no errors
    And the result should be false

  Scenario: Chargeback Query None
    Given an undefined message type indicator
    When I determine if the message type indicator is a chargeback
    Then there should be an error containing Undefined message type indicator!
