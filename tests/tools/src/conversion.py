
def is_boolean_string(string: str) -> bool:
    """Check if a string is a boolean."""
    return string in ['false', 'False', 'FALSE', 'true', 'True', 'TRUE']


def string_to_boolean(string: str) -> bool:
    """Convert a string to a boolean."""
    return string not in ['false', 'False', 'FALSE']


def normalize_binary_string(binary_string: str) -> str:
    """Convert a binary string to a readable string."""
    # Remove any spaces
    binary_string = binary_string.replace(' ', '')

    length = len(binary_string)
    if (length % 8) != 0:
        prefix = '0' * (8 - (length % 8))
        binary_string = prefix + binary_string
        length = len(binary_string)

    if length == 0:
        return ''

    binary_string = binary_string[::-1]

    ans = []
    for i in range(0, len(binary_string), 4):
        ans.append(binary_string[i:i + 4])

    return ' '.join(ans)[::-1]


def binary_string_to_bytes(s: str) -> bytes:
    s = s.replace(' ', '')  # Remove spaces
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


def hex_string_to_byte_array(hex_string: str) -> bytearray:
    """Convert a hex string to a byte array."""
    length = len(hex_string)

    if length % 2 != 0:
        hex_string = '0' + hex_string

    return bytearray.fromhex(hex_string)
