"""
Generate customer sessions.

Each session represents one attempt by a customer
to place an order on QuickBite.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config import RANDOM_SEED

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def _coin(probability: float) -> bool:
    """Return True with given probability."""
    return random.random() < probability


def _conversion_probability(
    rating: float,
    delivery_fee: float,
    device: str,
    loyalty: str,
    weekend: bool,
) -> float:
    """
    Hidden probability model.

    This is never exposed to the analyst.
    """

    p = 0.42

    if rating >= 4.6:
        p += 0.08

    elif rating >= 4.3:
        p += 0.04

    if delivery_fee > 70:
        p -= 0.10

    elif delivery_fee > 50:
        p -= 0.05

    if device == "Android":
        p -= 0.03

    if loyalty == "High":
        p += 0.06

    if weekend:
        p += 0.02

    return min(max(p, 0.10), 0.90)


def generate_sessions(
    users: pd.DataFrame,
    restaurants: pd.DataFrame,
    n_sessions: int = 100000,
) -> pd.DataFrame:

    rows = []

    start = datetime(2025, 1, 1)

    for session_id in range(1, n_sessions + 1):

        user = users.sample(1).iloc[0]
        restaurant = restaurants.sample(1).iloc[0]

        session_date = start + timedelta(
            minutes=random.randint(0, 365 * 24 * 60)
        )

        weekend = session_date.weekday() >= 5

        probability = _conversion_probability(
            restaurant["rating"],
            restaurant["delivery_fee"],
            user["device"],
            user["loyalty_segment"],
            weekend,
        )

        restaurant_view = True

        menu_view = _coin(0.96)

        cart = menu_view and _coin(probability + 0.15)

        checkout = cart and _coin(probability)

        payment = checkout and _coin(probability - 0.05)

        completed = payment and _coin(probability)

        rows.append(
            {
                "session_id": session_id,
                "user_id": user["user_id"],
                "restaurant_id": restaurant["restaurant_id"],
                "session_date": session_date,
                "city": user["city"],
                "device": user["device"],
                "restaurant_view": restaurant_view,
                "menu_view": menu_view,
                "cart": cart,
                "checkout": checkout,
                "payment": payment,
                "completed": completed,
                "delivery_fee": restaurant["delivery_fee"],
                "restaurant_rating": restaurant["rating"],
                "session_duration_sec": random.randint(60, 1400),
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":

    from src.generators.restaurants import generate_restaurants
    from src.generators.users import generate_users

    users = generate_users()

    restaurants = generate_restaurants()

    sessions = generate_sessions(
        users,
        restaurants,
        n_sessions=10000,
    )

    print(sessions.head())

    print()

    print(sessions["completed"].mean())
