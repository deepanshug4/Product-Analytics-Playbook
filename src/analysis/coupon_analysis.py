"""
Coupon Effectiveness Analysis
"""

from pathlib import Path

import matplotlib.pyplot as plt

SQL_DIR = Path("sql")
OUTPUT_DIR = Path("outputs/charts")
TABLE_DIR = Path("outputs/tables")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def coupon_analysis(con):

    query = (SQL_DIR / "05_coupon_analysis.sql").read_text()

    df = con.execute(query).df()

    print("\n===== COUPON ANALYSIS =====\n")
    print(df)

    df.to_csv(
        TABLE_DIR / "coupon_analysis.csv",
        index=False
    )

    plt.figure(figsize=(6,4))

    plt.bar(
        df["coupon_group"],
        df["avg_total_paid"]
    )

    plt.title("Average Amount Paid by Coupon Usage")
    plt.xlabel("Customer Group")
    plt.ylabel("Average Amount Paid")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "coupon_analysis.png",
        dpi=300
    )

    plt.close()

    print("\n✓ Coupon chart saved.")

    return df