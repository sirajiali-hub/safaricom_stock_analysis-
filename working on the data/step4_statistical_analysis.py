import pandas as pd
import numpy as np

print("="*50)
print("STEP 4: Statistical Analysis & Insights")
print("="*50)

# Load data
df = pd.read_csv('safaricom_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'])
print("\n✓ Data loaded")

# Create Year_Month column
df['Year_Month'] = df['Date'].dt.to_period('M')
print("✓ Created Year_Month column")

# Remove NaN values for calculations
returns = df['Daily_Return'].dropna()

print("\n" + "="*50)
print("📈 PERFORMANCE METRICS")
print("="*50)

# Total return
total_return = df['Cumulative_Return'].iloc[-1]
print(f"\n💰 Total Return (2 years): {total_return:.2f}%")

# Annualized return
days = len(df)
annualized_return = ((1 + total_return/100) ** (252/days) - 1) * 100
print(f"📅 Annualized Return: {annualized_return:.2f}%")

# Average daily return
avg_daily_return = returns.mean()
print(f"📊 Average Daily Return: {avg_daily_return:.3f}%")

# Win rate (percentage of positive days)
positive_days = (returns > 0).sum()
total_days = len(returns)
win_rate = (positive_days / total_days) * 100
print(f"✅ Win Rate: {win_rate:.2f}% ({positive_days}/{total_days} days)")

print("\n" + "="*50)
print("⚠️  RISK METRICS")
print("="*50)

# Volatility (standard deviation)
daily_volatility = returns.std()
annualized_volatility = daily_volatility * np.sqrt(252)
print(f"\n📉 Daily Volatility: {daily_volatility:.2f}%")
print(f"📉 Annualized Volatility: {annualized_volatility:.2f}%")

# Max drawdown
cumulative = (1 + df['Daily_Return'].fillna(0)/100).cumprod()
running_max = cumulative.expanding().max()
drawdown = (cumulative - running_max) / running_max * 100
max_drawdown = drawdown.min()
print(f"⬇️  Maximum Drawdown: {max_drawdown:.2f}%")

# Sharpe Ratio (assuming 5% risk-free rate)
risk_free_rate = 5.0  # Kenya T-Bill rate ~5%
excess_return = annualized_return - risk_free_rate
sharpe_ratio = excess_return / annualized_volatility if annualized_volatility > 0 else 0
print(f"📐 Sharpe Ratio: {sharpe_ratio:.2f}")

# Value at Risk (VaR) - 95% confidence
var_95 = np.percentile(returns, 5)
print(f"⚡ VaR (95%): {var_95:.2f}% (worst expected loss on 95% of days)")

print("\n" + "="*50)
print("📊 DISTRIBUTION METRICS")
print("="*50)

print(f"\n🔢 Best Single Day: +{returns.max():.2f}%")
print(f"🔻 Worst Single Day: {returns.min():.2f}%")
print(f"📏 Median Daily Return: {returns.median():.3f}%")
print(f"📊 Standard Deviation: {returns.std():.2f}%")

# Skewness and Kurtosis
skewness = returns.skew()
kurtosis = returns.kurtosis()
print(f"📈 Skewness: {skewness:.2f} {'(right-skewed)' if skewness > 0 else '(left-skewed)'}")
print(f"📊 Kurtosis: {kurtosis:.2f} {'(fat tails)' if kurtosis > 0 else '(thin tails)'}")

print("\n" + "="*50)
print("📅 TIME-BASED ANALYSIS")
print("="*50)

# Best/Worst months
monthly_returns = df.groupby('Year_Month')['Daily_Return'].sum()
best_month = monthly_returns.idxmax()
worst_month = monthly_returns.idxmin()
print(f"\n🏆 Best Month: {best_month} (+{monthly_returns.max():.2f}%)")
print(f"📉 Worst Month: {worst_month} ({monthly_returns.min():.2f}%)")

# Day of week analysis
dow_returns = df.groupby('Day_of_Week')['Daily_Return'].mean()
dow_sorted = dow_returns.sort_values(ascending=False)
print(f"\n📆 Average Returns by Day of Week:")
for day, ret in dow_sorted.items():
    print(f"   {day}: {ret:.3f}%")

print("\n" + "="*50)
print("💡 KEY INSIGHTS")
print("="*50)

print(f"""
✅ POSITIVE INDICATORS:
   • Stock gained {total_return:.2f}% over 2 years
   • Win rate of {win_rate:.1f}% (more up days than down)
   • Sharpe ratio of {sharpe_ratio:.2f} {'(good risk-adjusted returns)' if sharpe_ratio > 1 else '(moderate risk-adjusted returns)'}

⚠️  RISK CONSIDERATIONS:
   • Maximum drawdown was {abs(max_drawdown):.2f}%
   • Daily volatility of {daily_volatility:.2f}%
   • Worst single day loss: {returns.min():.2f}%

📊 INVESTMENT PROFILE:
   • Annualized Return: {annualized_return:.2f}%
   • Annualized Risk: {annualized_volatility:.2f}%
   • Best performing day: {dow_sorted.index[0]}
""")

# Save summary to text file
with open('analysis_summary.txt', 'w') as f:
    f.write("SAFARICOM STOCK ANALYSIS SUMMARY\n")
    f.write("="*50 + "\n\n")
    f.write(f"Period: {df['Date'].min().date()} to {df['Date'].max().date()}\n")
    f.write(f"Total Return: {total_return:.2f}%\n")
    f.write(f"Annualized Return: {annualized_return:.2f}%\n")
    f.write(f"Volatility: {annualized_volatility:.2f}%\n")
    f.write(f"Sharpe Ratio: {sharpe_ratio:.2f}\n")
    f.write(f"Max Drawdown: {max_drawdown:.2f}%\n")
    f.write(f"Win Rate: {win_rate:.2f}%\n")

print("\n✓ Saved summary to: analysis_summary.txt")

print("\n" + "="*50)
print("✓ Step 4 Complete!")
print("="*50)
print("\nNext: Create a final dashboard/report!")