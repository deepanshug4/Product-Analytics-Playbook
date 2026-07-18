"""
Visualization utilities for Product Analytics Playbook.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = Path("outputs/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_funnel(funnel: pd.DataFrame):

    plt.figure(figsize=(8, 5))

    plt.barh(
        funnel["Stage"],
        funnel["Users"],
    )

    plt.title("QuickBite Order Funnel")
    plt.xlabel("Number of Sessions")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "funnel_chart.png",
        dpi=300,
    )

    plt.close()

    print("✓ Funnel chart saved.")
