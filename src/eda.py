# import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

# load the built-in Diamond dataset from seaborn
print("Loading dataset from Seaborn...")
df = sns.load_dataset('diamonds')

# save it to our data folder as CSV
df.to_csv('data/diamonds.csv', index=False)
print("✅Data saved to 'data/diamonds.csv'\n")

# Health check
print("--- 📊 DATA HEALTH CHECK ---\n")

# .info() tells us the column names, how many rows we have, and data types
print("1. Data Structure and Missing Values:")
df.info()

print("\n" + "="*40 + "\n")

# .describe() gives us basic math statistics (average, price, min/max carat, etc)
print("2. Mathematical Summary: ")
print(df.describe().to_markdown())

print("\n" + "="*40 + "\n")

# check exact number for missing values
print("3. Total Missing Valuse per Column:")
print(df.isnull().sum())

print("\n✅ Health Check Complete!")

# data cleaning 
print("\n--- 🧹 DATA CLEANING ---")
print(f"Original number of rows: {len(df)}")

# Remove rows where x, y, or z is 0 (because a diamond can't have 0 dimensions!)
df = df[(df['x'] != 0) & (df['y'] != 0) & (df['z'] != 0)]

print(f"Number of rows after cleaning 0-dimension diamonds: {len(df)}")
print("\n" + "="*40 + "\n")

# --- EXPLORATORY VISUALIZATIONS ---

# Set a beautiful theme for our Seaborn plots
sns.set_theme(style="whitegrid")

# Plot 1: Distribution of Diamond Prices (Histogram)
# This answers: What is the most common price range for diamonds?
plt.figure(figsize=(10, 5))
sns.histplot(df['price'], bins=50, kde=True, color='royalblue')
plt.title('Distribution of Diamond Prices', fontsize=16)
plt.xlabel('Price ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Save the plot to the screenshots folder!
plt.savefig('screenshots/price_distribution.png')
plt.close() # Close the plot so it doesn't overlap with the next one
print("📊 Plot 1 saved: screenshots/price_distribution.png")


# Plot 2: Count of Diamonds by Cut Quality (Countplot)
# This answers: Which cut quality is the most common?
plt.figure(figsize=(8, 5))
# We order it from Fair to Ideal so it looks like a logical progression
cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
sns.countplot(data=df, x='cut', hue='cut', palette='viridis', order=cut_order, legend=False)
plt.title('Number of Diamonds by Cut Quality', fontsize=16)
plt.xlabel('Cut Quality', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Save the plot
plt.savefig('screenshots/cut_count.png')
plt.close()
print("📊 Plot 2 saved: screenshots/cut_count.png")

print("\n✅ EDA Step 1 Complete!")

# --- BIVARIATE ANALYSIS (Finding Relationships) ---

print("\n--- 🤝 FINDING RELATIONSHIPS ---")

# Plot 3: Carat vs. Price (Scatter Plot)
# This answers: Does a heavier diamond (higher carat) cost more?
# We use a sample of 5,000 rows so the scatter plot renders fast and doesn't look like a giant blob
df_sample = df.sample(5000, random_state=42)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_sample, x='carat', y='price', hue='cut', palette='viridis', alpha=0.7)
plt.title('Diamond Price vs. Carat Weight', fontsize=16)
plt.xlabel('Carat (Weight)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.savefig('screenshots/carat_vs_price.png')
plt.close()
print("📊 Plot 3 saved: screenshots/carat_vs_price.png")


# Plot 4: Price by Cut Quality (Box Plot)
# This answers: How does the cut quality affect the price distribution?
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cut', y='price', hue='cut', palette='coolwarm', order=cut_order, legend=False)
plt.title('Price Distribution by Cut Quality', fontsize=16)
plt.xlabel('Cut Quality', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.savefig('screenshots/price_by_cut.png')
plt.close()
print("📊 Plot 4 saved: screenshots/price_by_cut.png")

print("\n✅ EDA Step 2 Complete!")

# --- MULTIVARIATE ANALYSIS (Correlation) ---

print("\n--- 🌡️ FINDING CORRELATIONS ---")

# Plot 5: Correlation Heatmap
# This answers: How strongly do all numeric variables relate to one another?
plt.figure(figsize=(10, 8))

# We only want to calculate correlation for numeric columns (not categories like 'cut')
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
corr_matrix = numeric_df.corr()

# Draw the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Diamond Features', fontsize=16)
plt.savefig('screenshots/correlation_heatmap.png')
plt.close()
print("📊 Plot 5 saved: screenshots/correlation_heatmap.png")

print("\n✅ EDA Step 3 (Final) Complete!")