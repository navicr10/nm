# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fYAOMCQeXl2gcsslkv2jNGIqasyImSON
"""

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv('house_prices_large.csv')  # Ensure this CSV is in your working directory

# Step 2: Define features and target
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Parking', 'Age']]
y = df['Price']

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 4: Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict
predictions = model.predict(X_test)

# Step 6: Display results
print("Predicted vs Actual Prices:")
for pred, actual in zip(predictions[:10], y_test.values[:10]):
    print(f"Predicted: ${pred:,.2f} | Actual: ${actual:,.2f}")

# Step 7: Evaluate
print("\nModel Performance:")
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("R² Score:", r2_score(y_test, predictions))

# Step 8: Plot
plt.scatter(y_test, predictions, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.grid(True)
plt.show()