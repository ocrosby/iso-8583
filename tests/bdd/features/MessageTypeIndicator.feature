# Created by omarcrosby at 3/10/23
Feature: MTI
  As a developer
  I want to be able to determine the meaning of a message type indicator
  So that I can determine the version of the ISO 8583 standard that a message conforms to

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

