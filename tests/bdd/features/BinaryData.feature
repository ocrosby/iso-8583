# Created by omarcrosby at 3/11/23
Feature: Binary Data
  As a developer
  I want to be able to manipulate binary data
  So that I can do cool things with BitMaps

  Scenario: Binary String Normalization Empty
    Given an empty binary string
    When I normalize the binary string
    Then there should be no errors
    And the result should be empty

  Scenario: Byte Array Creation
    When I create an array of 4 bytes
    Then there should be no errors
    And the result should be 00 00 00 00 in hexadecimal