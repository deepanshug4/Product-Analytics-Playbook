"""
Synthetic data generators for the Product Analytics Playbook.

Each generator creates one entity in the QuickBite data warehouse.

Available generators:
- Users
- Restaurants
- Sessions
- Orders
"""

from .users import generate_users
from .restaurants import generate_restaurants

__all__ = [
    "generate_users",
    "generate_restaurants",
]
