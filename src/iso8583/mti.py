from enum import Enum
from typing import Optional


class Purpose(Enum):
    Unknown = -1
    ReservedByIso = 0
    Authorization = 1
    Financial = 2
    File = 3
    ReversalAndChargeback = 4
    Reconciliation = 5
    Administrative = 6
    FeeCollection = 7
    NetworkManagement = 8


class Version(Enum):
    ReservedByIso = -1
    ISO_8583_1987 = 0
    ISO_8583_1993 = 1
    ISO_8583_2003 = 2
    NationalUse = 8
    PrivateUse = 9


RESERVED_BY_ISO = 'Reserved by ISO'


VERSION_MAPPING = {
    '0': Version.ISO_8583_1987,
    '1': Version.ISO_8583_1993,
    '2': Version.ISO_8583_2003,
    '3': Version.ReservedByIso,
    '4': Version.ReservedByIso,
    '5': Version.ReservedByIso,
    '6': Version.ReservedByIso,
    '7': Version.ReservedByIso,
    '8': Version.NationalUse,
    '9': Version.PrivateUse
}

PURPOSE_MAPPING = {
    '0': Purpose.ReservedByIso,
    '1': Purpose.Authorization,
    '2': Purpose.Financial,
    '3': Purpose.File,
    '4': Purpose.ReversalAndChargeback,
    '5': Purpose.Reconciliation,
    '6': Purpose.Administrative,
    '7': Purpose.FeeCollection,
    '8': Purpose.NetworkManagement,
    '9': Purpose.ReservedByIso
}


def version(message_type_indicator: str) -> Optional[str]:
    """Return the version of the message type indicator."""
    target_digit = message_type_indicator[0]

    if not target_digit.isdigit():
        raise ValueError(f'Invalid message type indicator "{message_type_indicator}"!')

    return VERSION_MAPPING.get(target_digit, None)


def purpose(message_type_indicator: str) -> Optional[Purpose]:
    """Returns the overall purpose of the message.

    Position two of the MTI specifies the overall purpose of the message.

    Authorization (x1xx)
        Determine if funds are available, get an approval but do not post to account for reconciliation.
        Dual message system (DMS), awaits file exchange for posting to the account.

    Financial (x2xx)
        Determine if funds are available, get an approval and post directly to the account.
        Single message system (SMS), no file exchange after this.

    File (x3xx)
        Used for hot-card, TMS and other exchanges

    Reversal and Chargeback
        Reversal (x4x0 or x4x1): Reverses the action of the previous authorization.
        Chargeback (x4x2 or x4x3): Charges back a previously cleared financial message.

    Reconciliation
        Transmit settlement information message.

    Administrative
        Transmits administrative advice.  Often used for failure messages (e.g., message reject or failure to apply).

    Network
        Used for secure key exchange, logon, echo test and other network functions.
    """
    target_digit = message_type_indicator[1]

    if not target_digit.isdigit():
        raise ValueError(f'Invalid message type indicator "{message_type_indicator}"!')

    return PURPOSE_MAPPING.get(target_digit, None)
