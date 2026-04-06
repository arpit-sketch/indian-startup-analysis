# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('startup_funding.csv')

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
df.head()
# %%
print(df.isnull().sum())
# %%
# imp columns
df = df[['Startup Name', 'Industry Vertical', 'City  Location', 'Investors Name', 'Amount in USD']]
df = df.dropna(subset=['Amount in USD'])
df = df.reset_index(drop=True)

print("Rows remaining:", len(df))
print("\nMissing values now:")
print(df.isnull().sum())
# %%
print(df['Amount in USD'].dtype)
print("\nSample values:")
print(df['Amount in USD'].head(10))
# %%
df['Amount in USD'] = df['Amount in USD'].str.replace(',', '')
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')
df = df.dropna(subset=['Amount in USD'])
df = df.reset_index(drop=True)

print("Rows remaining:", len(df))
print("\nData type now:", df['Amount in USD'].dtype)
print("\nSample values:")
print(df['Amount in USD'].head(10))
# %%
top_sectors = df['Industry Vertical'].value_counts().head(10)
print(top_sectors)

# %%
df['Industry Vertical'] = df['Industry Vertical'].str.strip()
df['Industry Vertical'] = df['Industry Vertical'].replace({
    'ECommerce': 'eCommerce',
    'E-Commerce': 'eCommerce',
    'ecommerce': 'eCommerce'
})

top_sectors = df['Industry Vertical'].value_counts().head(10)
print(top_sectors)
# %%
plt.figure(figsize=(16, 8))
top_sectors.plot(kind='bar', color='green')

plt.title('Top 10 Sectors by Number of Funding Deals in India')
plt.xlabel('Sector')
plt.ylabel('Number of Deals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('top_sectors.png')
plt.show()
# %%
top_cities = df['City  Location'].value_counts().head(10)
print(top_cities)
# %%
df['City  Location'] = df['City  Location'].str.strip()
df['City  Location'] = df['City  Location'].replace({
    'Bengaluru': 'Bangalore',
    'Gurugram': 'Gurgaon',
    'New Delhi': 'Delhi',
    'Noida': 'Delhi'
})

top_cities = df['City  Location'].value_counts().head(10)
print(top_cities)
# %%
plt.figure(figsize=(12, 6))
top_cities.plot(kind='bar', color='coral')

plt.title('Top 10 Cities by Number of Startup Funding Deals')
plt.xlabel('City')
plt.ylabel('Number of Deals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('top_cities.png')
plt.show()
# %%
sector_funding = df.groupby('Industry Vertical')['Amount in USD'].sum()
sector_funding = sector_funding.sort_values(ascending=False).head(10)
print(sector_funding)
# %%
# Convert to billions and round to 2 decimal places
sector_funding_billions = (sector_funding / 1_000_000_000).round(2)
print(sector_funding_billions)
# %%
df['Industry Vertical'] = df['Industry Vertical'].replace({
    'FinTech': 'Finance',
    'Fintech': 'Finance'
})

sector_funding = df.groupby('Industry Vertical')['Amount in USD'].sum()
sector_funding_billions = (sector_funding / 1_000_000_000).round(2)
sector_funding_billions = sector_funding_billions.sort_values(ascending=False).head(10)
print(sector_funding_billions)
# %%
plt.figure(figsize=(12, 6))
sector_funding_billions.plot(kind='bar', color='yellow')

plt.title('Top 10 Sectors by Total Funding Amount (in Billions USD)')
plt.xlabel('Sector')
plt.ylabel('Total Funding (Billion USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('sector_funding_amount.png')
plt.show()
# %%
amounts = df['Amount in USD'].values

avg_deal = np.mean(amounts)
median_deal = np.median(amounts)
largest_deal = np.max(amounts)
smallest_deal = np.min(amounts)

print(f"Average deal size:  ${avg_deal/1_000_000:.2f} Million")
print(f"Median deal size:   ${median_deal/1_000_000:.2f} Million")
print(f"Largest deal:       ${largest_deal/1_000_000:.2f} Million")
print(f"Smallest deal:      ${smallest_deal/1_000_000:.2f} Million")
# %%
top_sector_by_deals = df['Industry Vertical'].value_counts().idxmax()
top_sector_by_deals_count = df['Industry Vertical'].value_counts().max()

top_sector_by_money = sector_funding_billions.idxmax()
top_sector_by_money_amount = sector_funding_billions.max()

top_city = df['City  Location'].value_counts().idxmax()
top_city_count = df['City  Location'].value_counts().max()

print("=" * 50)
print("KEY FINDINGS — INDIAN STARTUP FUNDING ANALYSIS")
print("=" * 50)
print(f"Total deals analyzed: {len(df)}")
print(f"Top sector by deals: {top_sector_by_deals} ({top_sector_by_deals_count} deals)")
print(f"Top sector by money: {top_sector_by_money} (${top_sector_by_money_amount:.2f} Billion)")
print(f"Top city: {top_city} ({top_city_count} deals)")
print(f"Typical deal size: ${median_deal/1_000_000:.2f} Million (median)")
print(f"Largest single deal: ${largest_deal/1_000_000:.2f} Million")
print("=" * 50)
# %%
