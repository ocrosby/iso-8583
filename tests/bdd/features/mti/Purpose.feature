# Created by omarcrosby at 3/11/23
Feature: Message Type Indicator Purpose
  As a developer
  I want to be able to determine the purpose of the message type indicator
  So that I know the overall purpose of the message

  Scenario: Purpose x0xx
    Given a message type indicator x0xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.ReservedByIso

  Scenario: Purpose x1xx
    Given a message type indicator x1xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.Authorization

  Scenario: Purpose x2xx
    Given a message type indicator x2xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.Financial

  Scenario: Purpose x3xx
    Given a message type indicator x3xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.File

  Scenario: Purpose x4xx
    Given a message type indicator x4xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.ReversalAndChargeback

  Scenario: Purpose x5xx
    Given a message type indicator x5xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.Reconciliation

  Scenario: Purpose x6xx
    Given a message type indicator x6xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.Administrative

  Scenario: Purpose x7xx
    Given a message type indicator x7xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.FeeCollection

  Scenario: Purpose x8xx
    Given a message type indicator x8xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.NetworkManagement

  Scenario: Purpose x9xx
    Given a message type indicator x9xx
    When I determine the indicators purpose
    Then there should be no errors
    And the result should be Purpose.ReservedByIso

  Scenario: Purpose xZxx
    Given a message type indicator xZxx
    When I determine the indicators purpose
    Then there should be an error containing Invalid message type indicator
