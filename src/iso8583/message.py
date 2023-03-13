from typing import Optional


class Message:
    data: Optional[str]

    def __init__(self):
        self.data = None

    @staticmethod
    def create_from_hex_string(hex_string: str) -> 'Message':
        message = Message()
        message.data = bytearray.fromhex(hex_string)

        return message

