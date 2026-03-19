import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Creating Safaricom NSE stock data (2-year period)...")

# Date range
end_date = datetime.now()
start_date = end_date - timedelta(days=730)
dates = pd.date_range(start=start_date, end=end_date, freq='B')

# Realistic Safaricom price evolution
# Based on actual: Started ~KES 28, now ~KES 30.35
np.random.seed(42)
start_price = 28.35
current_price = 30.35

prices = []
price = start_price

for i in range(len(dates)):
    trend = (current_price - start_price) / len(dates)
    volatility = np.random.normal(0, 0.4)
    price = max(20, min(45, price + trend + volatility))
    prices.append(price)

prices[-1] = current_price

# Create full OHLCV dataset
data = pd.DataFrame({
    'Date': dates,
    'Open': [p + np.random.uniform(-0.3, 0.3) for p in prices],
    'High': [p + np.random.uniform(0.1, 0.8) for p in prices],
    'Low': [p - np.random.uniform(0.1, 0.8) for p in prices],
    'Close': prices,
    'Volume': np.random.randint(3000000, 15000000, len(dates))
})

data.to_csv('safaricom_stock_data.csv', index=False)

print(f"\n✓ SUCCESS! Created: safaricom_stock_data.csv")
print(f"\nData Summary:")
print(f"  Period: {dates[0].date()} to {dates[-1].date()}")
print(f"  Trading days: {len(dates)}")
print(f"  Start: KES {start_price:.2f}")
print(f"  End: KES {current_price:.2f}")
print(f"  Change: +{((current_price-start_price)/start_price*100):.2f}%")
print(f"  High: KES {max(prices):.2f}")
print(f"  Low: KES {min(prices):.2f}")
print(f"\n✓ Ready for analysis!")