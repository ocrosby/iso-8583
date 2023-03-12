from enum import Enum
from typing import List


class BitMapType(Enum):
    Binary = 1
    Hexadecimal = 2


def field_number_to_byte_offset(field_number: int) -> int:
    return (field_number - 1) // 8


def field_number_to_bit_offset(field_number: int) -> int:
    return (field_number - 1) % 8


def binary_string_to_byte(binary_string: str) -> int:
    return int(binary_string, 2)


def hexadecimal_string_to_byte(hexadecimal_string: str) -> int:
    return int(hexadecimal_string, 16)


class BitMap:
    mutable_bytes: bytearray

    def __init__(self, size_in_bytes: int = 8):
        self.mutable_bytes = bytearray(size_in_bytes)

    def test(self, field_number: int) -> bool:
        byte_offset = field_number_to_byte_offset(field_number)
        bit_offset = field_number_to_bit_offset(field_number)

        return self.mutable_bytes[byte_offset] & (1 << (8 - bit_offset - 1)) != 0

    @property
    def present(self) -> List[int]:
        result = []

        for i in range(1, 65):
            if self.test(i):
                result.append(i)

        return result

    @staticmethod
    def create_from_binary_string(binary_string: str) -> 'BitMap':
        bitmap = BitMap()
        bitmap.mutable_bytes = bytearray([binary_string_to_byte(x) for x in binary_string.split(' ')])

        return bitmap

    @staticmethod
    def create_from_hex_string(hex_string: str) -> 'BitMap':
        bitmap = BitMap()
        bitmap.mutable_bytes = bytearray([hexadecimal_string_to_byte(x) for x in hex_string.split(' ')])

        return bitmap

    @staticmethod
    def parse(bitmap_value: str, bitmap_type: BitMapType) -> List[int]:
        if bitmap_type == BitMapType.Binary:
            return BitMap.create_from_binary_string(bitmap_value).present
        elif bitmap_type == BitMapType.Hexadecimal:
            return BitMap.create_from_hex_string(bitmap_value).present
        else:
            raise Exception('Unknown bitmap type')
