"""
Funnel Analysis

Business Question:
Where are users dropping off during the ordering journey?
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from utils.analysis_utils import run_query

OUTPUT_DIR = Path("outputs/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def funnel_analysis(con):
    """Run funnel analysis and generate a funnel chart."""

    result = run_query(
        con,
        "01_funnel_analysis.sql",
        "funnel_analysis.csv"
    )

    total = result.loc[0, "total_sessions"]

    funnel = pd.DataFrame({
        "Stage": [
            "Restaurant View",
            "Menu View",
            "Cart",
            "Checkout",
            "Payment",
            "Completed"
        ],
        "Users": [
            result.loc[0, "restaurant_views"],
            result.loc[0, "menu_views"],
            result.loc[0, "cart_additions"],
            result.loc[0, "checkouts"],
            result.loc[0, "payments"],
            result.loc[0, "completed_orders"],
        ]
    })

    funnel["Conversion %"] = (
        funnel["Users"] / total * 100
    ).round(1)

    print("\n===== FUNNEL ANALYSIS =====\n")
    print(funnel)

    plt.figure(figsize=(8, 5))

    plt.barh(
        funnel["Stage"],
        funnel["Users"]
    )

    plt.title("QuickBite Order Funnel")
    plt.xlabel("Sessions")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "funnel_analysis.png",
        dpi=300
    )

    plt.close()

    print("\n✓ Funnel chart saved.")

    return funnel