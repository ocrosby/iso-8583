import pytest

from src.iso8583 import bits
from src.iso8583.bits import BitMapType


class TestFieldNumberToByteOffset:
    def test_field_number_1(self):
        assert bits.field_number_to_byte_offset(1) == 0

    def test_field_number_2(self):
        assert bits.field_number_to_byte_offset(2) == 0

    def test_field_number_3(self):
        assert bits.field_number_to_byte_offset(3) == 0

    def test_field_number_4(self):
        assert bits.field_number_to_byte_offset(4) == 0

    def test_field_number_5(self):
        assert bits.field_number_to_byte_offset(5) == 0

    def test_field_number_6(self):
        assert bits.field_number_to_byte_offset(6) == 0

    def test_field_number_7(self):
        assert bits.field_number_to_byte_offset(7) == 0

    def test_field_number_8(self):
        assert bits.field_number_to_byte_offset(8) == 0

    def test_field_number_9(self):
        assert bits.field_number_to_byte_offset(9) == 1


class TestFieldNumberToBitOffset:
    def test_field_number_1(self):
        assert bits.field_number_to_bit_offset(1) == 0

    def test_field_number_2(self):
        assert bits.field_number_to_bit_offset(2) == 1

    def test_field_number_3(self):
        assert bits.field_number_to_bit_offset(3) == 2

    def test_field_number_4(self):
        assert bits.field_number_to_bit_offset(4) == 3

    def test_field_number_5(self):
        assert bits.field_number_to_bit_offset(5) == 4

    def test_field_number_6(self):
        assert bits.field_number_to_bit_offset(6) == 5

    def test_field_number_7(self):
        assert bits.field_number_to_bit_offset(7) == 6

    def test_field_number_8(self):
        assert bits.field_number_to_bit_offset(8) == 7

    def test_field_number_9(self):
        assert bits.field_number_to_bit_offset(9) == 0


class TestBinaryStringToByte:
    def test_binary_string_00000000(self):
        assert bits.binary_string_to_byte('00000000') == 0

    def test_binary_string_00000001(self):
        assert bits.binary_string_to_byte('00000001') == 1

    def test_binary_string_00000010(self):
        assert bits.binary_string_to_byte('00000010') == 2

    def test_binary_string_00000011(self):
        assert bits.binary_string_to_byte('00000011') == 3

    def test_binary_string_00000100(self):
        assert bits.binary_string_to_byte('00000100') == 4

    def test_binary_string_00000101(self):
        assert bits.binary_string_to_byte('00000101') == 5

    def test_binary_string_00000110(self):
        assert bits.binary_string_to_byte('00000110') == 6

    def test_binary_string_00000111(self):
        assert bits.binary_string_to_byte('00000111') == 7

    def test_binary_string_00001000(self):
        assert bits.binary_string_to_byte('00001000') == 8

    def test_binary_string_00001001(self):
        assert bits.binary_string_to_byte('00001001') == 9

    def test_binary_string_00001010(self):
        assert bits.binary_string_to_byte('00001010') == 10


class TestTest:
    def test_field_number_1_affirmative(self):
        # Arrange
        bitmap_value = '10000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(1)

        # Assert
        assert result

    def test_field_number_1_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(1)

        # Assert
        assert not result

    def test_field_number_2_affirmative(self):
        # Arrange
        bitmap_value = '01000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(2)

        # Assert
        assert result

    def test_field_number_2_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(2)

        # Assert
        assert not result

    def test_field_number_3_affirmative(self):
        # Arrange
        bitmap_value = '00100000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(3)

        # Assert
        assert result

    def test_field_number_3_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(3)

        # Assert
        assert not result

    def test_field_number_4_affirmative(self):
        # Arrange
        bitmap_value = '00010000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(4)

        # Assert
        assert result

    def test_field_number_4_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(4)

        # Assert
        assert not result

    def test_field_number_5_affirmative(self):
        # Arrange
        bitmap_value = '00001000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(5)

        # Assert
        assert result

    def test_field_number_5_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(5)

        # Assert
        assert not result

    def test_field_number_6_affirmative(self):
        # Arrange
        bitmap_value = '00000100'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(6)

        # Assert
        assert result

    def test_field_number_6_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(6)

        # Assert
        assert not result

    def test_field_number_7_affirmative(self):
        # Arrange
        bitmap_value = '00000010'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(7)

        # Assert
        assert result

    def test_field_number_7_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(7)

        # Assert
        assert not result

    def test_field_number_8_affirmative(self):
        # Arrange
        bitmap_value = '00000001'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(8)

        # Assert
        assert result

    def test_field_number_8_negative(self):
        # Arrange
        bitmap_value = '00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(8)

        # Assert
        assert not result

    def test_field_number_9_affirmative(self):
        # Arrange
        bitmap_value = '00000000 10000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(9)

        # Assert
        assert result

    def test_field_number_9_negative(self):
        # Arrange
        bitmap_value = '00000000 00000000'
        bitmap = bits.BitMap.create_from_binary_string(bitmap_value)

        # Act
        result = bitmap.test(9)

        # Assert
        assert not result


def test_bitmap_parse_unknown():
    with pytest.raises(Exception) as err:
        bits.BitMap.parse('00000000', BitMapType.Unknown)

    assert err.value.args[0] == 'Unknown bitmap type'
