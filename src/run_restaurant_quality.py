from load_data import create_connection, load_tables
from analysis.restaurant_quality import restaurant_quality_analysis

con = create_connection()
load_tables(con)

restaurant_quality_analysis(con)