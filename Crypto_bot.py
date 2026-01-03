import requests
from config import url, currencies

def get_price(coin: str):
    params = {
        "ids": coin,
        "vs_currencies":currencies
    }

    response = requests.get(url, params=params, timeout=15)
    data = response.json()

    if coin in data:
        return data[coin]["usd"], data[coin]["inr"]
    
    else: return "Error"

