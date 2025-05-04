import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'app', 'database', 'btc_price.db'))

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM btc_price", conn)
print(df.head())

print('----------------------')
print(df.isnull().sum())
print('----------------------')
print(df.describe())