"""
Project-wide constants and enumerations.
"""

from enum import Enum


class Device(str, Enum):
    ANDROID = "Android"
    IOS = "iOS"
    DESKTOP = "Desktop"


class Loyalty(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class FunnelStage(str, Enum):
    LANDING = "landing"
    RESTAURANT = "restaurant"
    MENU = "menu"
    CART = "cart"
    CHECKOUT = "checkout"
    PAYMENT = "payment"
    COMPLETED = "completed"
