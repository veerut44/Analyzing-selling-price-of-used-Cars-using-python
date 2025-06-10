# 📊 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 👁️‍🗨️ Display Plots Inline (for Jupyter)
%matplotlib inline

# 📂 Load Data
df = pd.read_csv('used_cars.csv')  # Ensure the CSV is in the same folder or give full path

# 👀 Display First Few Rows
print("🔍 Preview of the Dataset:")
print(df.head())

# 📈 Basic Info and Stats
print("\n🧾 Dataset Information:")
print(df.info())
print("\n📊 Statistical Summary:")
print(df.describe())

# ✅ Handle Missing Data (Optional)
# df.dropna(inplace=True)

# 📌 Price vs Year (Scatter Plot)
plt.figure(figsize=(10,6))
sns.scatterplot(x='Year', y='Price', hue='Brand', data=df, palette='tab10')
plt.title("Selling Price by Year", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Selling Price (INR)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 📊 Fuel Type Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Fuel_Type', data=df, palette='Set2')
plt.title("Distribution of Fuel Types", fontsize=14)
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 💰 Brand vs Average Price
avg_price = df.groupby("Brand")['Price'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
avg_price.plot(kind='bar', color='skyblue')
plt.title("Average Selling Price by Brand", fontsize=14)
plt.ylabel("Price (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🔥 Heatmap of Correlation
plt.figure(figsize=(6,5))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# ✨ Interactive Scatter Plot: Year vs Price
fig = px.scatter(df, x='Year', y='Price', color='Brand',
                 hover_data=['Model', 'Kilometers_Driven'],
                 title="Interactive: Price vs Year by Brand")
fig.show()
