"""
Generate synthetic restaurant data for QuickBite.

Author: Deepanshu Gupta
"""

from __future__ import annotations

import random

import numpy as np
import pandas as pd

from config import (
    CITIES,
    N_RESTAURANTS,
    RANDOM_SEED,
)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

CUISINES = [
    "Indian",
    "Chinese",
    "Italian",
    "Pizza",
    "Burger",
    "South Indian",
    "Desserts",
    "Cafe",
    "Healthy",
    "Mexican",
]

PRICE_TIERS = ["Budget", "Mid", "Premium"]


def generate_restaurants(
    n_restaurants: int = N_RESTAURANTS,
) -> pd.DataFrame:
    """
    Generate synthetic restaurant information.
    """

    ratings = np.clip(
        np.random.normal(4.2, 0.35, n_restaurants),
        2.8,
        5.0,
    )

    df = pd.DataFrame(
        {
            "restaurant_id": np.arange(1, n_restaurants + 1),
            "city": np.random.choice(CITIES, n_restaurants),
            "cuisine": np.random.choice(CUISINES, n_restaurants),
            "rating": np.round(ratings, 1),
            "price_tier": np.random.choice(
                PRICE_TIERS,
                n_restaurants,
                p=[0.45, 0.40, 0.15],
            ),
            "delivery_fee": np.round(
                np.random.uniform(19, 89, n_restaurants),
                2,
            ),
        }
    )

    df["estimated_delivery_time"] = (
        18
        + (5 - df["rating"]) * 6
        + np.random.randint(0, 12, n_restaurants)
    ).round().astype(int)

    df["is_premium_partner"] = (
        (df["rating"] >= 4.6)
        & (df["price_tier"] == "Premium")
    )

    return df


if __name__ == "__main__":

    restaurants = generate_restaurants()

    print(restaurants.head())

    print()

    print(restaurants.describe(include="all"))
