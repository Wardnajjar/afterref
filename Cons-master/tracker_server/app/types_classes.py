from enum import Enum

from enum import Enum

class PlugType(Enum):
    MEROSS = 1

        TUYA (int): Tuya Cloud (additional).
    """

    MEROSS = 1
    TUYA = 2

class EType(Enum):
    """
    Enumeration representing energy types of devices.
    Attributes:
        NONE (int): Represents a device with no specific energy type.
        SHIFTABLE (int): Represents a shiftable device.
        PHANTOM (int): Represents a phantom device (all phantom devices are shiftable).
    """
    NONE = 1
    SHIFTABLE = 2
    PHANTOM = 3


class NotifType(Enum):
    """
    Enumeration representing types of notifications.
    Attributes:
        CREDS (int): Represents a notification related to incorrect login credentials.
        DISCONNECTION (int): Represents a notification related to device disconnection.
        GOAL (int): Represents a notification related to energy goals.
        PEAK (int): Represents a notification related to peak time energy usage.
        PHANTOM (int): Represents a notification related to phantom power usage.
        BASELINE (int): Represents a notification related to baseline energy threshold.
    """
    CREDS = 1
    DISCONNECTION = 2
    GOAL = 3
    PEAK = 4
    PHANTOM = 5
    BASELINE = 6

    """

    CREDS = 1
    DISCONNECTION = 2
    GOAL = 3
    PEAK = 4
    PHANTOM = 5
    BASELINE = 6
