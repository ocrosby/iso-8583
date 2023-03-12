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


class Function(Enum):
    Request = 0
    RequestResponse = 1
    Advice = 2
    AdviceResponse = 3
    Notification = 4
    NotificationAcknowledgement = 5
    Instruction = 6
    InstructionAcknowledgement = 7
    ReservedByIso = 8


class Origin(Enum):
    Acquirer = 0
    AcquirerRepeat = 1
    Issuer = 2
    IssuerRepeat = 3
    Other = 4
    ReservedByIso = 5


class Version(Enum):
    ReservedByIso = -1
    ISO_8583_1987 = 0
    ISO_8583_1993 = 1
    ISO_8583_2003 = 2
    NationalUse = 8
    PrivateUse = 9


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

FUNCTION_MAPPING = {
    '0': Function.Request,
    '1': Function.RequestResponse,
    '2': Function.Advice,
    '3': Function.AdviceResponse,
    '4': Function.Notification,
    '5': Function.NotificationAcknowledgement,
    '6': Function.Instruction,
    '7': Function.InstructionAcknowledgement,
    '8': Function.ReservedByIso,
    '9': Function.ReservedByIso
}

ORIGIN_MAPPING = {
    '0': Origin.Acquirer,
    '1': Origin.AcquirerRepeat,
    '2': Origin.Issuer,
    '3': Origin.IssuerRepeat,
    '4': Origin.Other,
    '6': Origin.ReservedByIso,
}


class MessageTypeIndicator:
    value: Optional[str]

    def __init__(self, value: Optional[str]):
        if value:
            self.value = value[:4]
        else:
            self.value = None

    @property
    def version(self) -> Version:
        """Return the version of the message type indicator."""
        target_digit = self.value[0]

        if not target_digit.isdigit():
            raise ValueError(f'Invalid message type indicator "{self.value}"!')

        return VERSION_MAPPING.get(target_digit, None)

    @property
    def purpose(self) -> Purpose:
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
            Transmits administrative advice.  Often used for failure messages
            (e.g., message reject or failure to apply).

        Network
            Used for secure key exchange, logon, echo test and other network functions.
        """
        target_digit = self.value[1]

        if not target_digit.isdigit():
            raise ValueError(f'Invalid message type indicator "{self.value}"!')

        return PURPOSE_MAPPING.get(target_digit, None)

    @property
    def function(self) -> Function:
        target_digit = self.value[2]

        if not target_digit.isdigit():
            raise ValueError(f'Invalid message type indicator "{self.value}"!')

        return FUNCTION_MAPPING.get(target_digit, None)

    @property
    def origin(self) -> Origin:
        target_digit = self.value[3]

        if not target_digit.isdigit():
            raise ValueError(f'Invalid message type indicator "{self.value}"!')

        return ORIGIN_MAPPING.get(target_digit, None)

    def is_reversal(self) -> bool:
        """Returns whether the message type indicator is a reversal."""
        if self.value is None:
            raise ValueError('Undefined message type indicator!')

        if self.purpose != Purpose.ReversalAndChargeback:
            return False

        target_digit = self.value[3]

        return target_digit in ['0', '1']

    def is_chargeback(self) -> bool:
        """Returns whether the message type indicator is a chargeback."""
        if self.value is None:
            raise ValueError('Undefined message type indicator!')

        if self.purpose != Purpose.ReversalAndChargeback:
            return False

        target_digit = self.value[3]

        return target_digit in ['2', '3']
