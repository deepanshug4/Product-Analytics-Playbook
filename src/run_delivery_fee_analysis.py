from load_data import create_connection, load_tables
from analysis.delivery_fee import delivery_fee_analysis

con = create_connection()

load_tables(con)

delivery_fee_analysis(con)