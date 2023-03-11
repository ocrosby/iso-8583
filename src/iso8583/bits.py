class BitMap:
    mutable_bytes: bytearray

    def __init__(self, size_in_bytes: int = 8):
        self.mutable_bytes = bytearray(size_in_bytes)

    @staticmethod
    def createFromHexString(hexString: str) -> 'BitMap':
        bitmap = BitMap()
        bitmap.mutable_bytes = bytearray(bytes.fromhex(hexString))

        return bitmap

    @staticmethod
    def createFromBytes(data: bytes) -> 'BitMap':
        bitmap = BitMap()
        bitmap.mutable_bytes = bytearray(data)

        return bitmap

    @staticmethod
    def createFromBinaryString(binaryString: str) -> 'BitMap':
        bitmap = BitMap()
        bitmap.mutable_bytes = bytearray(bytes.fromhex(hex(int(binaryString, 2))[2:]))

        return bitmap
