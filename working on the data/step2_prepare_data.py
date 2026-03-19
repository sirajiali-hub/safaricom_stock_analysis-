import pandas as pd
import numpy as np

print("="*50)
print("STEP 2: Cleaning and Preparing Data")
print("="*50)

# Load the data
df = pd.read_csv('safaricom_stock_data.csv')
print("\n✓ Data loaded")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("✓ Converted Date column to datetime format")

# Sort by date (just to be sure)
df = df.sort_values('Date').reset_index(drop=True)
print("✓ Sorted data by date")

# Calculate daily returns (percentage change)
df['Daily_Return'] = df['Close'].pct_change() * 100
print("✓ Calculated daily returns")

# Calculate price change (in KES)
df['Price_Change'] = df['Close'].diff()
print("✓ Calculated price changes")

# Calculate moving averages
df['MA_7'] = df['Close'].rolling(window=7).mean()  # 1-week MA
df['MA_30'] = df['Close'].rolling(window=30).mean()  # 1-month MA
df['MA_90'] = df['Close'].rolling(window=90).mean()  # 3-month MA
print("✓ Calculated moving averages (7, 30, 90 days)")

# Calculate volatility (rolling standard deviation)
df['Volatility_30'] = df['Daily_Return'].rolling(window=30).std()
print("✓ Calculated 30-day volatility")

# Calculate cumulative returns
df['Cumulative_Return'] = (1 + df['Daily_Return']/100).cumprod() - 1
df['Cumulative_Return'] = df['Cumulative_Return'] * 100
print("✓ Calculated cumulative returns")

# Add year, month, day columns for easier analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_of_Week'] = df['Date'].dt.day_name()
print("✓ Added time-based columns")

# Display the enhanced dataset
print(f"\n📊 Enhanced Dataset:")
print(f"   Total columns: {len(df.columns)}")
print(f"   New columns added: {len(df.columns) - 6}")

print(f"\n📋 Sample of cleaned data:")
print(df[['Date', 'Close', 'Daily_Return', 'MA_30', 'Volatility_30']].tail(10))

# Key insights
print(f"\n💡 Key Insights:")
print(f"   Average Daily Return: {df['Daily_Return'].mean():.3f}%")
print(f"   Best Day Gain: {df['Daily_Return'].max():.2f}%")
print(f"   Worst Day Loss: {df['Daily_Return'].min():.2f}%")
print(f"   Average Volatility: {df['Volatility_30'].mean():.2f}%")
print(f"   Total Return (2 years): {df['Cumulative_Return'].iloc[-1]:.2f}%")

# Save cleaned data
df.to_csv('safaricom_cleaned.csv', index=False)
print(f"\n✓ Saved cleaned data to: safaricom_cleaned.csv")

print("\n" + "="*50)
print("✓ Step 2 Complete!")
print("="*50)
print("\nNext: We'll create visualizations!")