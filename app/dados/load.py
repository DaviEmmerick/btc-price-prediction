from extract import bitcoin_price
import sqlite3
import os

price = bitcoin_price()
#print(f"Preço do Bitcoin: ${price}")

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'app', 'database', 'btc_price.db'))
conn = sqlite3.connect(db_path)
c = conn.cursor()

print("Conectado ao banco de dados")

c.execute(
    'INSERT INTO btc_price (price, date_part, time_part) VALUES (?, date("now"), time("now"))',
    (price,)
)
conn.commit()
conn.close()