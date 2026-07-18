from load_data import create_connection, load_tables
from analysis.funnel import funnel_analysis

con = create_connection()
load_tables(con)

funnel_analysis(con)