"""
Basic analytics for the QuickBite datasets.
"""

import duckdb
import pandas as pd
from pathlib import Path
from visualization import plot_funnel
from load_data import create_connection, load_tables

DATA_DIR = Path("data/synthetic")
SQL_DIR = Path("sql")


def run_funnel_analysis(con):
    """Run funnel analysis and calculate stage conversion rates."""

    query = open(SQL_DIR / "01_funnel_analysis.sql").read()
    result = con.execute(query).df()

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

    return funnel


def main():

    con = create_connection()
    load_tables(con)
    funnel = run_funnel_analysis(con)
    plot_funnel(funnel)


if __name__ == "__main__":
    main()
