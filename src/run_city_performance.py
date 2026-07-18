from load_data import create_connection, load_tables
from analysis.city_performance import city_performance_analysis

con = create_connection()
load_tables(con)

city_performance_analysis(con)