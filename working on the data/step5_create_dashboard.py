import pandas as pd
import base64

print("="*50)
print("STEP 5: Creating Professional Dashboard")
print("="*50)

# Load data
df = pd.read_csv('safaricom_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'])
print("\n✓ Data loaded")

# Calculate key metrics
total_return = df['Cumulative_Return'].iloc[-1]
current_price = df['Close'].iloc[-1]
start_price = df['Close'].iloc[0]
high_price = df['Close'].max()
low_price = df['Close'].min()
avg_volume = df['Volume'].mean()

returns = df['Daily_Return'].dropna()
win_rate = (returns > 0).sum() / len(returns) * 100
best_day = returns.max()
worst_day = returns.min()
volatility = returns.std()

print("✓ Calculated metrics")

# Encode images to base64 for embedding
def image_to_base64(filepath):
    try:
        with open(filepath, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

print("✓ Encoding chart images...")

# Create HTML dashboard
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safaricom Stock Analysis Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }}
        
        .metric-card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }}
        
        .metric-label {{
            font-size: 0.9em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }}
        
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            color: #1e3c72;
        }}
        
        .metric-change {{
            font-size: 0.9em;
            margin-top: 5px;
        }}
        
        .positive {{
            color: #10b981;
        }}
        
        .negative {{
            color: #ef4444;
        }}
        
        .charts-section {{
            padding: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            margin-bottom: 30px;
            color: #1e3c72;
            border-left: 5px solid #667eea;
            padding-left: 15px;
        }}
        
        .chart-container {{
            margin-bottom: 40px;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .chart-container img {{
            width: 100%;
            height: auto;
            border-radius: 10px;
        }}
        
        .insights-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
        }}
        
        .insight-box {{
            background: rgba(255,255,255,0.1);
            border-left: 4px solid white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }}
        
        .insight-box h3 {{
            margin-bottom: 10px;
        }}
        
        .footer {{
            background: #1e3c72;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        @media (max-width: 768px) {{
            .metrics-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>📊 Safaricom Stock Analysis</h1>
            <p>Comprehensive 2-Year Performance Report</p>
            <p style="font-size: 0.9em; margin-top: 10px;">
                Period: {df['Date'].min().strftime('%B %d, %Y')} - {df['Date'].max().strftime('%B %d, %Y')}
            </p>
        </div>
        
        <!-- Key Metrics -->
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Current Price</div>
                <div class="metric-value">KES {current_price:.2f}</div>
                <div class="metric-change {'positive' if total_return > 0 else 'negative'}">
                    {'+' if total_return > 0 else ''}{total_return:.2f}% Total Return
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-label">Price Range</div>
                <div class="metric-value">{low_price:.2f} - {high_price:.2f}</div>
                <div class="metric-change">KES Spread: {high_price - low_price:.2f}</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-label">Win Rate</div>
                <div class="metric-value">{win_rate:.1f}%</div>
                <div class="metric-change">Positive Trading Days</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-label">Volatility</div>
                <div class="metric-value">{volatility:.2f}%</div>
                <div class="metric-change">Daily Standard Deviation</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-label">Best Day</div>
                <div class="metric-value positive">+{best_day:.2f}%</div>
                <div class="metric-change">Single Day Gain</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-label">Worst Day</div>
                <div class="metric-value negative">{worst_day:.2f}%</div>
                <div class="metric-change">Single Day Loss</div>
            </div>
        </div>
        
        <!-- Charts Section -->
        <div class="charts-section">
            <h2 class="section-title">📈 Visual Analysis</h2>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Price Trend with Moving Averages</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/1_price_trend.png')}" alt="Price Trend">
            </div>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Cumulative Returns</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/4_cumulative_returns.png')}" alt="Cumulative Returns">
            </div>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Daily Returns Distribution</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/2_returns_distribution.png')}" alt="Returns Distribution">
            </div>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Trading Volume</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/3_volume.png')}" alt="Volume">
            </div>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Volatility Analysis</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/6_volatility.png')}" alt="Volatility">
            </div>
            
            <div class="chart-container">
                <h3 style="margin-bottom: 15px;">Monthly Performance</h3>
                <img src="data:image/png;base64,{image_to_base64('charts/5_monthly_performance.png')}" alt="Monthly Performance">
            </div>
        </div>
        
        <!-- Insights Section -->
        <div class="insights-section">
            <h2 style="margin-bottom: 30px;">💡 Key Insights</h2>
            
            <div class="insight-box">
                <h3>📊 Performance Summary</h3>
                <p>Safaricom stock showed a total return of {total_return:.2f}% over the 2-year period, 
                moving from KES {start_price:.2f} to KES {current_price:.2f}. The stock achieved a win rate 
                of {win_rate:.1f}%, indicating more positive trading days than negative.</p>
            </div>
            
            <div class="insight-box">
                <h3>⚠️ Risk Profile</h3>
                <p>The daily volatility of {volatility:.2f}% suggests {'moderate' if volatility < 2 else 'high'} 
                price fluctuations. The best single-day gain was {best_day:.2f}%, while the worst loss was 
                {worst_day:.2f}%.</p>
            </div>
            
            <div class="insight-box">
                <h3>📈 Trading Activity</h3>
                <p>Average daily trading volume reached {avg_volume:,.0f} shares, indicating 
                {'strong' if avg_volume > 5000000 else 'moderate'} market liquidity and investor interest.</p>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <p>Dashboard created with Python | Data Analysis Portfolio Project</p>
            <p style="font-size: 0.9em; margin-top: 10px;">
                Generated: {pd.Timestamp.now().strftime('%B %d, %Y at %I:%M %p')}
            </p>
        </div>
    </div>
</body>
</html>
"""

# Save dashboard
with open('safaricom_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\n✓ Dashboard created successfully!")
print("\n" + "="*50)
print("✓ Step 5 Complete!")
print("="*50)
print("""
🎉 PORTFOLIO PROJECT COMPLETE! 🎉

Files created:
📁 safaricom_stock_data.csv - Original data
📁 safaricom_cleaned.csv - Cleaned data with features
📁 analysis_summary.txt - Statistical summary
📂 charts/ - 6 visualization charts
📊 safaricom_dashboard.html - Interactive dashboard

🌐 To view your dashboard:
   1. Open 'safaricom_dashboard.html' in your browser
   2. Share it in your portfolio
   3. Upload to GitHub Pages for online hosting

Next steps for portfolio:
✅ Add README.md explaining the project
✅ Upload to GitHub
✅ Add to your portfolio website
""")