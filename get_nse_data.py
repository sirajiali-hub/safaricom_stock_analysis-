import requests
import pandas as pd
from datetime import datetime, timedelta

# Get your free API key from RapidAPI
API_KEY = "YOUR_RAPIDAPI_KEY_HERE"

url = "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "nairobi-stock-exchange-nse.p.rapidapi.com"
}

print("Fetching Safaricom data from NSE...")
response = requests.get(url, headers=headers)
data = response.json()

# Find Safaricom in the data
for stock in data:
    if 'Safaricom' in stock.get('company', ''):
        print(f"\n✓ Found: {stock}")
        
# Save to CSV
df = pd.DataFrame(data)
df.to_csv('nse_stocks_today.csv', index=False)
print("\n✓ Saved: nse_stocks_today.csv")