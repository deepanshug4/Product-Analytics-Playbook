"""
Generate orders from completed customer sessions.

Only completed sessions become successful orders.
"""

from __future__ import annotations

import random

import numpy as np
import pandas as pd

from config import RANDOM_SEED

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def generate_orders(
    sessions: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate orders from completed sessions.
    """

    completed = sessions[sessions["completed"]].copy()

    if completed.empty:
        raise ValueError("No completed sessions found.")

    order_ids = np.arange(1, len(completed) + 1)

    basket = np.random.gamma(
        shape=2.8,
        scale=230,
        size=len(completed),
    )

    coupon = np.random.choice(
        [True, False],
        len(completed),
        p=[0.30, 0.70],
    )

    discount = np.where(
        coupon,
        np.random.uniform(40, 180, len(completed)),
        0,
    )

    surge = np.random.choice(
        [1.0, 1.2, 1.5],
        len(completed),
        p=[0.80, 0.15, 0.05],
    )

    ratings = np.clip(
        np.random.normal(4.4, 0.45, len(completed)),
        1,
        5,
    )

    df = pd.DataFrame(
        {
            "order_id": order_ids,
            "session_id": completed["session_id"].values,
            "user_id": completed["user_id"].values,
            "restaurant_id": completed["restaurant_id"].values,
            "order_timestamp": completed["session_date"].values,
            "basket_value": basket.round(2),
            "coupon_used": coupon,
            "discount": discount.round(2),
            "delivery_fee": completed["delivery_fee"].values,
            "surge_multiplier": surge,
            "customer_rating": ratings.round(1),
        }
    )

    df["total_paid"] = (
        df["basket_value"]
        + df["delivery_fee"] * df["surge_multiplier"]
        - df["discount"]
    ).round(2)

    return df


if __name__ == "__main__":

    from src.generators.restaurants import generate_restaurants
    from src.generators.sessions import generate_sessions
    from src.generators.users import generate_users

    users = generate_users()

    restaurants = generate_restaurants()

    sessions = generate_sessions(
        users,
        restaurants,
        n_sessions=10000,
    )

    orders = generate_orders(sessions)

    print(orders.head())

    print()

    print(f"Orders generated : {len(orders)}")
