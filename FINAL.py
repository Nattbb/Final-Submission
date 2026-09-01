import os

# Rename the file from .zip to .csv as it appears to be a misnamed CSV file
os.rename('/content/WDI_CSV.zip', '/content/WDI_CSV.csv')

print("Renamed '/content/WDI_CSV.zip' to '/content/WDI_CSV.csv'")

import pandas as pd
import numpy as np
from google.colab import files

# ==========================================
# 1. UPLOAD FILE
# ==========================================
print("Please upload your extracted WDI CSV file (e.g., WDIData.csv or WDI_CSV.csv):")
uploaded = files.upload()

# Get the exact filename dynamically
filename = list(uploaded.keys())[0]
print(f"\nLoading '{filename}' into Pandas...")

df = pd.read_csv(filename)

# ==========================================
# 2. DEFINE TARGET METRICS & FILTER
# ==========================================
# Map World Bank Indicator Codes to clean variable names for Tableau
target_indicators = {
    'NY.GDP.MKTP.CD': 'GDP_USD',
    'NY.GDP.PCAP.CD': 'GDP_Per_Capita',
    'SP.DYN.LE00.IN': 'Life_Expectancy',
    'SP.POP.TOTL': 'Total_Population',
    'EN.ATM.CO2E.PC': 'CO2_Per_Capita',
    'IT.NET.USER.ZS': 'Internet_Users_Pct'
}

# Filter for relevant indicators
df_filtered = df[df['Indicator Code'].isin(target_indicators.keys())].copy()
df_filtered['Indicator_Clean'] = df_filtered['Indicator Code'].map(target_indicators)

# ==========================================
# 3. UNPIVOT (MELT) YEAR COLUMNS (2000–2023)
# ==========================================
# Find all available year columns present in the file
available_years = [str(col) for col in range(2000, 2024) if str(col) in df_filtered.columns]

id_cols = ['Country Name', 'Country Code', 'Indicator_Clean']

df_melted = pd.melt(
    df_filtered,
    id_vars=id_cols,
    value_vars=available_years,
    var_name='Year',
    value_name='Value'
)

# Convert types
df_melted['Year'] = df_melted['Year'].astype(int)
df_melted['Value'] = pd.to_numeric(df_melted['Value'], errors='coerce')

# ==========================================
# 4. REMOVE REGIONAL / NON-COUNTRY AGGREGATES
# ==========================================
non_countries = [
    'World', 'High income', 'Low income', 'Middle income', 'Upper middle income',
    'Lower middle income', 'Sub-Saharan Africa', 'European Union', 'OECD members',
    'East Asia & Pacific', 'Latin America & Caribbean', 'Arab World', 
    'South Asia', 'North America', 'Middle East & North Africa'
]

df_melted = df_melted[~df_melted['Country Name'].isin(non_countries)]

# ==========================================
# 5. PIVOT INDICATORS INTO COLUMNS (TIDY FORMAT)
# ==========================================
df_tidy = df_melted.pivot_table(
    index=['Country Name', 'Country Code', 'Year'],
    columns='Indicator_Clean',
    values='Value'
).reset_index()

df_tidy.columns.name = None

# Drop rows where all target indicators are blank/NaN
indicator_cols = list(target_indicators.values())
df_tidy = df_tidy.dropna(subset=indicator_cols, how='all')

# Sort chronologically
df_tidy = df_tidy.sort_values(by=['Country Name', 'Year']).reset_index(drop=True)

# ==========================================
# 6. EXPORT & DOWNLOAD CLEANED CSV
# ==========================================
output_filename = 'WDI_Cleaned_Data.csv'
df_tidy.to_csv(output_filename, index=False)

print(f"\nData cleaning complete!")
print(f"Dataset Shape: {df_tidy.shape[0]} rows × {df_tidy.shape[1]} columns")
print("\nPreview of Cleaned Data:")
display(df_tidy.head())