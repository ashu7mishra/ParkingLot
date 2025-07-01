from enum import Enum


class ParkingLotStatus(Enum):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    FULL = 'FULL'
    UNDER_MAINTAINANCE = 'UNDER_MAINTAINANCE'


class GateType(Enum):
    ENTRY = 'ENTRY'
    EXIT = 'EXIT'


class GateStatus(Enum):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    UNDER_MAINTAINANCE = 'UNDER_MAINTAINANCE'


class FloorStatus(Enum):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    FULL = 'FULL'
    UNDER_MAINTAINANCE = 'UNDER_MAINTAINANCE'


class SlotStatus(Enum):
    FILLED = 'FILLED'
    EMPTY = 'EMPTY'
    BLOCKED = 'BLOCKED'
    RESERVED = 'RESERVED'


class VehicleType(Enum):
    CAR = 'CAR'
    BIKE = 'BIKE'
    BUS = 'BUS'
    TRUCK = 'TRUCK'


class BillStatus(Enum):
    PAID = 'PAID'
    PENDING = 'PENDING'
    PARTIALLY_PAID = 'PARTIALLY_PAID'


class PaymentMode(Enum):
    CASH = 'CASH'
    ONLINE = 'ONLINE'
    CARD = 'CARD'
    UPI = 'UPI'


class PaymentStatus(Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class SlotAssignmentStrategyEnum(Enum):
    RANDOM = 'RANDOM'


