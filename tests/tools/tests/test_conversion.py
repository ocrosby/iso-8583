import sys

from tests.tools.src import conversion


def test_is_boolean_string():
    """Test if a string is a boolean."""
    assert conversion.is_boolean_string('false')
    assert conversion.is_boolean_string('False')
    assert conversion.is_boolean_string('FALSE')
    assert conversion.is_boolean_string('true')
    assert conversion.is_boolean_string('True')
    assert conversion.is_boolean_string('TRUE')
    assert not conversion.is_boolean_string('foo')


def test_string_to_boolean():
    """Test converting a string to a boolean."""
    assert conversion.string_to_boolean('false') is False
    assert conversion.string_to_boolean('False') is False
    assert conversion.string_to_boolean('FALSE') is False
    assert conversion.string_to_boolean('true') is True
    assert conversion.string_to_boolean('True') is True
    assert conversion.string_to_boolean('TRUE') is True
    assert conversion.string_to_boolean('foo') is True


class TestBinaryStringToBytes:
    def test_0000_0000(self):
        assert conversion.binary_string_to_bytes('0000 0000') == b'\x00'

    def test_0000_0001(self):
        assert conversion.binary_string_to_bytes('0000 0001') == b'\x01'

    def test_0001_0000(self):
        assert conversion.binary_string_to_bytes('0001 0000') == b'\x10'

    def test_0000_1101(self):
        assert conversion.binary_string_to_bytes('0000 1101') == b'\x0d'

    def test_0011_0100(self):
        assert conversion.binary_string_to_bytes('0011 0100') == b'\x34'

    def test_1101_0011(self):
        assert conversion.binary_string_to_bytes('1101 0011') == b'\xd3'


class TestNormalizeBinaryString:
    def test_empty(self):
        assert conversion.normalize_binary_string('') == '0000 0000'

    def test_0(self):
        assert conversion.normalize_binary_string('0') == '0000 0000'

    def test_1(self):
        assert conversion.normalize_binary_string('1') == '0000 0001'

    def test_10(self):
        assert conversion.normalize_binary_string('10') == '0000 0010'

    def test_100(self):
        assert conversion.normalize_binary_string('100') == '0000 0100'

    def test_0000_0000(self):
        assert conversion.normalize_binary_string('0000 0000') == '0000 0000'

    def test_0000_0001(self):
        assert conversion.normalize_binary_string('0000 0001') == '0000 0001'

    def test_00010000(self):
        assert conversion.normalize_binary_string('00010000') == '0001 0000'

    def test_00001101(self):
        assert conversion.normalize_binary_string('00001101') == '0000 1101'

    def test_0011_0100(self):
        assert conversion.normalize_binary_string('0011 0100') == '0011 0100'

    def test_01_0011(self):
        assert conversion.normalize_binary_string('01 0011') == '0001 0011'



class TestHexStringToByteArray:
    def test_empty(self):
        # Arrange
        hex_string = ''

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b''

    def test_0(self):
        # Arrange
        hex_string = '0'

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b'\x00'

    def test_00(self):
        # Arrange
        hex_string = '00'

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b'\x00\x00'

    def test_01(self):
        # Arrange
        hex_string = '01'

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b'\x00\x01'

    def test_10(self):
        # Arrange
        hex_string = '10'

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b'\x01\x00'

    def test_deadbeef(self):
        """Test converting an empty string to a byte array."""
        # Arrange
        hex_string = 'deadbeef'

        # Act
        actual = conversion.hex_string_to_byte_array(hex_string)

        # Assert
        assert actual == b'\xde\xad\xbe\xef'
