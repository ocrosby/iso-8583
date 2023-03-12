# Created by omarcrosby at 3/11/23
Feature: Message Type Indicator Version
  As a developer
  I want to be able to determine the version of the message type indicator
  So that I am aware of the ISO 8583 version in which the message is encoded

  Scenario: Version 0xxx
    Given a message type indicator 0xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ISO_8583_1987

  Scenario: Version 1xxx
    Given a message type indicator 1xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ISO_8583_1993

  Scenario: Version 2xxx
    Given a message type indicator 2xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ISO_8583_2003

  Scenario: Version 3xxx
    Given a message type indicator 3xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ReservedByIso

  Scenario: Version 4xxx
    Given a message type indicator 4xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ReservedByIso

  Scenario: Version 5xxx
    Given a message type indicator 5xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ReservedByIso

  Scenario: Version 6xxx
    Given a message type indicator 6xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ReservedByIso

  Scenario: Version 7xxx
    Given a message type indicator 7xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.ReservedByIso

  Scenario: Version 8xxx
    Given a message type indicator 8xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.NationalUse

  Scenario: Version 9xxx
    Given a message type indicator 9xxx
    When I determine the indicators version
    Then there should be no errors
    And the result should be Version.PrivateUse

  Scenario: Version Zxxx
    Given a message type indicator Zxxx
    When I determine the indicators version
    Then there should be an error containing Invalid message type indicator
