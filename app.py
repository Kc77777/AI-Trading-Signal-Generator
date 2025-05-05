# 1. Load tools
import requests
import pandas as pd

# main variables
api_key = "BSU7XYEYBRA42W2Z"
interval = "15min"
symbol = "XAUUSD"

#url of xauusd
url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=XAU&to_symbol=USD&interval={interval}&apikey={api_key}&outputsize=compact"

response = requests.get(url)

print(response.status_code)  

data = response.json()

print(data.keys())

