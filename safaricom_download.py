# Install required library first: pip install yfinance pandas

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

print("Downloading Safaricom stock data...")

# Get data for last 2 years
end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # 2 years

# Download Safaricom data (Nairobi Stock Exchange)
ticker = "SCOM.NR"
data = yf.download(ticker, start=start_date, end=end_date)

if data.empty:
    print("No data found. Trying alternative ticker...")
    ticker = "SCOM.KE"
    data = yf.download(ticker, start=start_date, end=end_date)

# Save raw data
data.to_csv("safaricom_stock_data.csv")
print(f"✓ Saved raw data: safaricom_stock_data.csv")

# Basic analysis
print("\n--- SAFARICOM STOCK ANALYSIS ---")
print(f"Period: {start_date.date()} to {end_date.date()}")
print(f"Total trading days: {len(data)}")
print(f"\nPrice Summary:")
print(f"  Current Price: KES {data['Close'].iloc[-1]:.2f}")
print(f"  Highest Price: KES {data['High'].max():.2f}")
print(f"  Lowest Price: KES {data['Low'].min():.2f}")
print(f"  Average Price: KES {data['Close'].mean():.2f}")
print(f"\nPrice Change:")
print(f"  Start Price: KES {data['Close'].iloc[0]:.2f}")
print(f"  End Price: KES {data['Close'].iloc[-1]:.2f}")
change = ((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
print(f"  Total Change: {change:.2f}%")

print("\n✓ Analysis complete!")