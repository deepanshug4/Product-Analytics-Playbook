"""
Loads synthetic CSV datasets into DuckDB.

This keeps SQL queries independent of CSV files.
"""

from pathlib import Path
import duckdb

DATA_DIR = Path("data/synthetic")


def create_connection():
    """Create an in-memory DuckDB connection."""
    return duckdb.connect()


def load_tables(con):
    """Load all CSVs as DuckDB tables."""

    tables = {
        "users": "users_v1.csv",
        "restaurants": "restaurants_v1.csv",
        "sessions": "sessions_v1.csv",
        "orders": "orders_v1.csv",
    }

    for table, file in tables.items():
        con.execute(f"""
        CREATE OR REPLACE TABLE {table} AS
        SELECT *
        FROM read_csv_auto('{DATA_DIR / file}');
        """)

    print("✓ Loaded users")
    print("✓ Loaded restaurants")
    print("✓ Loaded sessions")
    print("✓ Loaded orders")


if __name__ == "__main__":

    con = create_connection()

    load_tables(con)

    print()

    print(con.execute("SHOW TABLES").fetchdf())