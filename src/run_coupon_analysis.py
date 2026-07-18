from load_data import create_connection, load_tables
from analysis.coupon_analysis import coupon_analysis

con = create_connection()
load_tables(con)

coupon_analysis(con)