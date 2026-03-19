import pandas as pd
import numpy as np

print("="*50)
print("STEP 1: Loading and Exploring Safaricom Data")
print("="*50)

# Load the data
df = pd.read_csv('safaricom_stock_data.csv')
print("\n✓ Data loaded successfully!")

# Basic information
print(f"\n📊 Dataset Overview:")
print(f"   Total records: {len(df)}")
print(f"   Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"   Columns: {list(df.columns)}")

# Display first few rows
print(f"\n📋 First 5 rows:")
print(df.head())

# Display last few rows
print(f"\n📋 Last 5 rows:")
print(df.tail())

# Data types
print(f"\n🔢 Data Types:")
print(df.dtypes)

# Check for missing values
print(f"\n❓ Missing Values:")
print(df.isnull().sum())

# Basic statistics
print(f"\n📈 Statistical Summary:")
print(df.describe())

# Price information
print(f"\n💰 Price Information:")
print(f"   Highest Close: KES {df['Close'].max():.2f}")
print(f"   Lowest Close: KES {df['Close'].min():.2f}")
print(f"   Average Close: KES {df['Close'].mean():.2f}")
print(f"   Current Price: KES {df['Close'].iloc[-1]:.2f}")

# Volume information
print(f"\n📊 Volume Information:")
print(f"   Highest Volume: {df['Volume'].max():,}")
print(f"   Lowest Volume: {df['Volume'].min():,}")
print(f"   Average Volume: {df['Volume'].mean():,.0f}")

print("\n" + "="*50)
print("✓ Step 1 Complete!")
print("="*50)