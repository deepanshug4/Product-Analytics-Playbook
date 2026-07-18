"""
City Performance Analysis
"""

from pathlib import Path

import matplotlib.pyplot as plt

SQL_DIR = Path("sql")
OUTPUT_DIR = Path("outputs/charts")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def city_performance_analysis(con):

    query = (SQL_DIR / "03_city_performance.sql").read_text()

    df = con.execute(query).df()

    print("\n===== CITY PERFORMANCE =====\n")
    print(df)

    plt.figure(figsize=(10, 5))

    plt.bar(df["city"], df["conversion_rate"])

    plt.title("Conversion Rate by City")
    plt.xlabel("City")
    plt.ylabel("Conversion Rate (%)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "city_performance.png",
        dpi=300
    )

    plt.close()

    print("\n✓ City chart saved.")

    return df