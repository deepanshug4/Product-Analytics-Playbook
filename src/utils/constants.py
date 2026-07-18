from enum import Enum

class Device(Enum):
    ANDROID = "Android"
    IOS = "iOS"
    DESKTOP = "Desktop"


class Loyalty(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
