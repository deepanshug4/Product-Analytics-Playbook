"""
Generate synthetic users for QuickBite.

The generated data intentionally contains realistic business behaviour
instead of random values.

Author: Deepanshu Gupta
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config import (
    CHANNELS,
    CITIES,
    DEVICES,
    N_USERS,
    RANDOM_SEED,
)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def _random_signup_date():
    """Return a random signup date within the previous 365 days."""

    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)

    delta = end - start

    return start + timedelta(days=random.randint(0, delta.days))


def _assign_loyalty():

    score = np.random.beta(2, 5)

    if score > 0.8:
        return "High"

    if score > 0.45:
        return "Medium"

    return "Low"


def generate_users(n_users: int = N_USERS) -> pd.DataFrame:
    """
    Generate synthetic user dataset.

    Parameters
    ----------
    n_users : int

    Returns
    -------
    pandas.DataFrame
    """

    df = pd.DataFrame(
        {
            "user_id": np.arange(1, n_users + 1),
            "signup_date": [_random_signup_date() for _ in range(n_users)],
            "city": np.random.choice(
                CITIES,
                n_users,
                p=[
                    0.18,
                    0.16,
                    0.15,
                    0.10,
                    0.09,
                    0.08,
                    0.08,
                    0.06,
                    0.05,
                    0.05,
                ],
            ),
            "device": np.random.choice(
                DEVICES,
                n_users,
                p=[0.58, 0.30, 0.12],
            ),
            "acquisition_channel": np.random.choice(
                CHANNELS,
                n_users,
                p=[0.34, 0.22, 0.18, 0.16, 0.10],
            ),
        }
    )

    df["platform"] = np.where(
        df["device"] == "Desktop",
        "Web",
        "App",
    )

    df["loyalty_segment"] = [
        _assign_loyalty() for _ in range(n_users)
    ]

    return df


if __name__ == "__main__":

    users = generate_users()

    print(users.head())

    print()

    print(users.describe(include="all"))
