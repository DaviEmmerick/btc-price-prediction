import pandas as pd
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'app', 'database', 'btc_price.db'))
conn = sqlite3.connect(db_path)

df = pd.read_sql_query('SELECT * FROM btc_price', conn)

print(df.columns) 

conn.execute('DROP TABLE IF EXISTS btc_price_new')
conn.execute('''
    CREATE TABLE btc_price_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        price REAL,
        date_part DATE,
        time_part TIME
    )
''')

for index, row in df.iterrows():
    date_value = row['date']
    date_part = date_value.split(' ')[0]  
    time_part = date_value.split(' ')[1]  

    conn.execute('''
        INSERT INTO btc_price_new (price, date_part, time_part)
        VALUES (?, ?, ?)
    ''', (row['price'], date_part, time_part))

conn.execute('DROP TABLE btc_price')
conn.execute('ALTER TABLE btc_price_new RENAME TO btc_price')

conn.commit()
conn.close()
