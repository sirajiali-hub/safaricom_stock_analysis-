import os
import shutil

print("Organizing project structure...")

# Create directories
os.makedirs('data', exist_ok=True)
os.makedirs('scripts', exist_ok=True)

# Move data files
data_files = ['safaricom_stock_data.csv', 'safaricom_cleaned.csv']
for file in data_files:
    if os.path.exists(file):
        shutil.move(file, f'data/{file}')
        print(f"✓ Moved {file} to data/")

# Move script files
script_files = [
    'step1_explore_data.py',
    'step2_prepare_data.py', 
    'step3_visualizations.py',
    'step4_statistical_analysis.py',
    'step5_create_dashboard.py'
]
for file in script_files:
    if os.path.exists(file):
        shutil.move(file, f'scripts/{file}')
        print(f"✓ Moved {file} to scripts/")

print("\n✓ Project structure organized!")
print("\nFinal structure:")
print("├── data/")
print("├── charts/")
print("├── scripts/")
print("├── safaricom_dashboard.html")
print("├── analysis_summary.txt")
print("├── README.md")
print("├── requirements.txt")
print("└── .gitignore")
