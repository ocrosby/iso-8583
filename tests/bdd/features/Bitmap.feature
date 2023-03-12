# Created by omarcrosby at 3/12/23
Feature: Bitmap
  As a developer
  I want to be able to manipulate bitmaps
  So that I can determine which other data elements or data element subfields are present elsewhere in the message

  Scenario: Parse - Field 1
    Given a binary bitmap value of 10000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 1 should be present
    And all fields other than 1 should be absent

  Scenario: Parse - Field 2
    Given a binary bitmap value of 01000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 2 should be present
    And all fields other than 2 should be absent

  Scenario: Parse - Field 3
    Given a binary bitmap value of 00100000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 3 should be present
    And all fields other than 3 should be absent

  Scenario: Parse - Field 4
    Given a binary bitmap value of 00010000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 4 should be present
    And all fields other than 4 should be absent

  Scenario: Parse - Field 5
    Given a binary bitmap value of 00001000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 5 should be present
    And all fields other than 5 should be absent

  Scenario: Parse - Field 6
    Given a binary bitmap value of 00000100 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 6 should be present
    And all fields other than 6 should be absent


  Scenario: Parse - Field 7
    Given a binary bitmap value of 00000010 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 7 should be present
    And all fields other than 7 should be absent


  Scenario: Parse - Field 8
    Given a binary bitmap value of 00000001 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 8 should be present
    And all fields other than 8 should be absent


  Scenario: Parse - Field 9
    Given a binary bitmap value of 00000000 10000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 9 should be present
    And all fields other than 9 should be absent

  Scenario: Parse - Field 10
    Given a binary bitmap value of 00000000 01000000 00000000 00000000 00000000 00000000 00000000 00000000
    When I parse the bitmap
    Then there should be no errors
    And field 10 should be present
    And all fields other than 10 should be absent

  Scenario: Wikipedia Example
    Given a hexadecimal bitmap value of 70 10 00 11 02 C0 48 04
    When I parse the bitmap
    Then there should be no errors
    And fields 2, 3, 4, 12, 28, 32, 39, 41, 42, 50, 53, 62 should be present
    And fields other than 2, 3, 4, 12, 28, 32, 39, 41, 42, 50, 53, 62 should be absent

