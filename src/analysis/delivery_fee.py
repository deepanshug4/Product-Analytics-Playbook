"""
Delivery fee analysis.

Business Question:
Does increasing delivery fee reduce conversion?
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

SQL_DIR = Path("sql")
OUTPUT_DIR = Path("outputs/charts")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def delivery_fee_analysis(con):

    query = open(
        SQL_DIR / "02_delivery_fee_analysis.sql"
    ).read()

    df = con.execute(query).df()

    print("\n===== DELIVERY FEE ANALYSIS =====\n")
    print(df)

    plt.figure(figsize=(7,4))

    plt.bar(
        df["fee_bucket"],
        df["conversion_rate"]
    )

    plt.title("Conversion Rate by Delivery Fee")

    plt.xlabel("Delivery Fee Bucket")

    plt.ylabel("Conversion %")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "delivery_fee.png",
        dpi=300
    )

    plt.close()

    print("\n✓ Chart saved.")

    return df