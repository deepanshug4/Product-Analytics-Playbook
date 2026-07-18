"""
Restaurant Quality Analysis
"""

from pathlib import Path

import matplotlib.pyplot as plt

SQL_DIR = Path("sql")
OUTPUT_DIR = Path("outputs/charts")
TABLE_DIR = Path("outputs/tables")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def restaurant_quality_analysis(con):

    query = (SQL_DIR / "04_restaurant_quality.sql").read_text()

    df = con.execute(query).df()

    print("\n===== RESTAURANT QUALITY =====\n")
    print(df)

    df.to_csv(
        TABLE_DIR / "restaurant_quality.csv",
        index=False
    )

    plt.figure(figsize=(7,4))

    plt.bar(
        df["rating_bucket"],
        df["conversion_rate"]
    )

    plt.title("Conversion Rate by Restaurant Rating")

    plt.xlabel("Restaurant Rating")

    plt.ylabel("Conversion (%)")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "restaurant_quality.png",
        dpi=300
    )

    plt.close()

    print("\n✓ Restaurant quality chart saved.")

    return df