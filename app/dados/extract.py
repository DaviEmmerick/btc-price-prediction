import requests


def bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    #print(data) 
    price = data['bitcoin']['usd']
    return price

print(f"Preço do Bitcoin: ${bitcoin_price()}")