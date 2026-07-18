"""
Global configuration for the Product Analytics Playbook.

Author: Deepanshu Gupta
"""

from pathlib import Path

# Root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

# SQL directory
SQL_DIR = PROJECT_ROOT / "sql"

# Output directories
OUTPUT_DIR = PROJECT_ROOT / "outputs"

CHART_DIR = OUTPUT_DIR / "charts"

REPORT_DIR = OUTPUT_DIR / "reports"

# Random seed
RANDOM_SEED = 42

# Dataset sizes

N_USERS = 50000

N_RESTAURANTS = 750

N_SESSIONS = 500000

N_ORDERS = 250000

# Cities

CITIES = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Kolkata",
    "Jaipur",
    "Ahmedabad",
    "Lucknow",
]

# Devices

DEVICES = [
    "Android",
    "iOS",
    "Desktop"
]

# Acquisition

CHANNELS = [
    "Organic",
    "Paid Search",
    "Instagram",
    "Referral",
    "Email",
]
