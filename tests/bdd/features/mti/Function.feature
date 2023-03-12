# Created by omarcrosby at 3/11/23
Feature: Message Type Indicator Function
  As a developer
  I want to be able to determine the function of the message type indicator
  So that I am aware of how the message should flow within the system

  Scenario: Function xx0x
    Given a message type indicator xx0x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.Request

  Scenario: Function xx1x
    Given a message type indicator xx1x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.RequestResponse

  Scenario: Function xx2x
    Given a message type indicator xx2x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.Advice

  Scenario: Function xx3x
    Given a message type indicator xx3x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.AdviceResponse

  Scenario: Function xx4x
    Given a message type indicator xx4x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.Notification

  Scenario: Function xx5x
    Given a message type indicator xx5x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.NotificationAcknowledgement

  Scenario: Function xx6x
    Given a message type indicator xx6x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.Instruction

  Scenario: Function xx7x
    Given a message type indicator xx7x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.InstructionAcknowledgement

  Scenario: Function xx8x
    Given a message type indicator xx8x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.ReservedByIso

  Scenario: Function xx9x
    Given a message type indicator xx9x
    When I determine the indicators function
    Then there should be no errors
    And the result should be Function.ReservedByIso

  Scenario: Function xxZx
    Given a message type indicator xxZx
    When I determine the indicators function
    Then there should be an error containing Invalid message type indicator
