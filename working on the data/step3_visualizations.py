import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*50)
print("STEP 3: Creating Visualizations")
print("="*50)

# Load cleaned data
df = pd.read_csv('safaricom_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'])
print("\n✓ Data loaded")

# Create a folder for charts
import os
os.makedirs('charts', exist_ok=True)
print("✓ Created 'charts' folder")

# Chart 1: Price Trend with Moving Averages
print("\n📊 Creating Chart 1: Price Trend with Moving Averages...")
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Close'], label='Close Price', linewidth=2, color='#1f77b4')
plt.plot(df['Date'], df['MA_7'], label='7-Day MA', linewidth=1.5, color='orange', alpha=0.7)
plt.plot(df['Date'], df['MA_30'], label='30-Day MA', linewidth=1.5, color='green', alpha=0.7)
plt.plot(df['Date'], df['MA_90'], label='90-Day MA', linewidth=1.5, color='red', alpha=0.7)
plt.title('Safaricom Stock Price (2-Year Trend)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (KES)', fontsize=12)
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/1_price_trend.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/1_price_trend.png")
plt.close()

# Chart 2: Daily Returns Distribution
print("\n📊 Creating Chart 2: Daily Returns Distribution...")
plt.figure(figsize=(12, 6))
plt.hist(df['Daily_Return'].dropna(), bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['Daily_Return'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Daily_Return"].mean():.2f}%')
plt.title('Distribution of Daily Returns', fontsize=16, fontweight='bold')
plt.xlabel('Daily Return (%)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/2_returns_distribution.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/2_returns_distribution.png")
plt.close()

# Chart 3: Volume Over Time
print("\n📊 Creating Chart 3: Trading Volume...")
plt.figure(figsize=(14, 6))
plt.bar(df['Date'], df['Volume'], color='teal', alpha=0.6, width=1)
plt.title('Trading Volume Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volume', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/3_volume.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/3_volume.png")
plt.close()

# Chart 4: Cumulative Returns
print("\n📊 Creating Chart 4: Cumulative Returns...")
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Cumulative_Return'], linewidth=2, color='green')
plt.fill_between(df['Date'], df['Cumulative_Return'], alpha=0.3, color='green')
plt.title('Cumulative Returns (2 Years)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Cumulative Return (%)', fontsize=12)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/4_cumulative_returns.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/4_cumulative_returns.png")
plt.close()

# Chart 5: Monthly Average Price
print("\n📊 Creating Chart 5: Monthly Performance...")
df['Year_Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Year_Month')['Close'].mean()

plt.figure(figsize=(14, 6))
monthly_avg.plot(kind='bar', color='coral', alpha=0.7)
plt.title('Average Monthly Price', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Price (KES)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/5_monthly_performance.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/5_monthly_performance.png")
plt.close()

# Chart 6: Volatility Over Time
print("\n📊 Creating Chart 6: Volatility Analysis...")
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Volatility_30'], linewidth=2, color='purple')
plt.title('30-Day Rolling Volatility', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volatility (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/6_volatility.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: charts/6_volatility.png")
plt.close()

print("\n" + "="*50)
print("✓ Step 3 Complete!")
print("="*50)
print("\n📁 All charts saved in the 'charts' folder")
print("   1. Price trend with moving averages")
print("   2. Daily returns distribution")
print("   3. Trading volume")
print("   4. Cumulative returns")
print("   5. Monthly performance")
print("   6. Volatility analysis")
print("\nNext: Statistical Analysis!")