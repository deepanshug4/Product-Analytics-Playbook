"""
Shared utilities for running SQL analyses.
"""

from pathlib import Path

SQL_DIR = Path("sql")
TABLE_DIR = Path("outputs/tables")

TABLE_DIR.mkdir(parents=True, exist_ok=True)


def run_query(con, sql_file, output_csv=None):
    """
    Execute a SQL file and optionally save the result.
    """

    query = (SQL_DIR / sql_file).read_text()

    df = con.execute(query).df()

    if output_csv:
        df.to_csv(
            TABLE_DIR / output_csv,
            index=False
        )

    return df
