import sqlite3
import os
from extract import bitcoin_price

path = 'btc-price-prediction/app/database/btc_price.db'

os.makedirs(os.path.dirname(path), exist_ok=True)

conn = sqlite3.connect(path)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS btc_price (price REAL, date TEXT)')
print("Conectado ao banco de dados")

price = bitcoin_price()
c.execute('INSERT INTO btc_price (price, date) VALUES (?, datetime("now"))', (price,))
conn.commit()
conn.close()