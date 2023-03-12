import sys
import pytest

def test_creating_4_bytes():
    """Test creating 4 bytes.

    So an immutable array of bytes of size 4 takes 37 bytes of memory!
    """
    # Act
    empty_bytes = bytes(4)  # bytes created this way are immutable

    # Assert
    assert empty_bytes == b'\x00\x00\x00\x00'
    assert type(empty_bytes) == bytes
    assert len(empty_bytes) == 4
    assert sys.getsizeof(empty_bytes) == 37


def test_data_bytes():
    """Test creating data bytes.

    So an immutable array of bytes of size 2 takes 35 bytes of memory!
    """
    # Act
    data_bytes = bytes(b'\xFF\xFF')

    # Assert
    assert data_bytes == b'\xff\xff'
    assert type(data_bytes) == bytes
    assert len(data_bytes) == 2
    assert sys.getsizeof(data_bytes) == 35


def test_creating_empty_byte_array():
    """Test creating a byte array.

    A byte array is mutable.

    An empty byte array takes 56 bytes of memory!
    """
    mutable_bytes = bytearray()

    assert mutable_bytes == b''
    assert type(mutable_bytes) == bytearray
    assert len(mutable_bytes) == 0
    assert sys.getsizeof(mutable_bytes) == 56


def test_creating_nonempty_byte_array():
    # Arrange
    count = 3

    # Act
    mutable_bytes = bytearray(count)

    # Assert
    assert mutable_bytes == b'\x00\x00\x00'
    assert type(mutable_bytes) == bytearray
    assert len(mutable_bytes) == 3
    assert sys.getsizeof(mutable_bytes) == 60


def test_creating_byte_array_from_bytes():
    """Test creating a byte array from bytes.

    So a mutable byte array of size 4 takes 61 bytes of memory!
    """

    # Arrange
    data_bytes = b'\xDE\xAD\xBE\xEF'

    # Act
    mutable_bytes = bytearray(data_bytes)

    # Assert
    assert mutable_bytes == b'\xde\xad\xbe\xef'
    assert type(mutable_bytes) == bytearray
    assert len(mutable_bytes) == 4
    assert sys.getsizeof(mutable_bytes) == 61


def test_manipulating_a_byte():
    """Test creating a byte array from bytes.

    So a mutable byte array of size 4 takes 61 bytes of memory!
    """

    # Arrange
    data_bytes = b'\xDE\xAD\xBE\xEF'

    # Act
    mutable_bytes = bytearray(data_bytes)
    mutable_bytes[0] = 0
    mutable_bytes.append(255)

    # Assert
    assert mutable_bytes == b'\x00\xad\xbe\xef\xff'
    assert type(mutable_bytes) == bytearray
    assert len(mutable_bytes) == 5
    assert sys.getsizeof(mutable_bytes) == 64

    # Accessing a slice of bytes
    assert mutable_bytes[0:2] == b'\x00\xad'


@pytest.mark.skip(reason='Not ready yet')
def test_byte_compliment():
    data_bytes = bytes(b'\x54')

    # Act
    compliemnt = ~data_bytes[0]
    compliment = hex(compliemnt)

    # Assert
    assert f'{compliemnt:b}' == 'AB'
    assert type(compliemnt) == int
