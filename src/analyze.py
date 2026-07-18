"""
Basic analytics for the QuickBite datasets.
"""

import duckdb
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/synthetic")
SQL_DIR = Path("sql")


def load_data(con):
    """Load CSV files into DuckDB."""

    con.execute(f"""
        CREATE OR REPLACE TABLE sessions AS
        SELECT *
        FROM read_csv_auto('{DATA_DIR / "sessions_v1.csv"}');
    """)


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

    con = duckdb.connect()

    load_data(con)

    run_funnel_analysis(con)


if __name__ == "__main__":
    main()
