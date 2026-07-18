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

    query = open(SQL_DIR / "01_funnel_analysis.sql").read()

    df = con.execute(query).df()

    print("\n===== FUNNEL METRICS =====\n")
    print(df)

    return df


def main():

    con = duckdb.connect()

    load_data(con)

    run_funnel_analysis(con)


if __name__ == "__main__":
    main()
