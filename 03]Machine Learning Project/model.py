import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Dataset with additional features
data = {
    'square_feet': [1500, 1800, 2400, 3000, 3500, 4000, 5000, 1600, 2200, 2500, 2800, 3300, 3800, 4500, 5500, 1400, 2100, 2300, 2600, 3200],
    'bedrooms': [3, 3, 4, 4, 5, 5, 6, 3, 4, 4, 5, 5, 6, 6, 7, 2, 3, 4, 4, 5],
    'bathrooms': [2, 2, 3, 3, 4, 4, 5, 2, 3, 3, 4, 4, 5, 5, 6, 1, 2, 3, 4, 5],
    'location': [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],  
    'age_of_house': [10, 15, 20, 5, 8, 3, 2, 12, 17, 22, 6, 9, 4, 1, 7, 25, 13, 18, 30, 10],
    'floor_number': [1, 1, 2, 2, 3, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'population_density': [1000, 1200, 900, 800, 1100, 950, 700, 1050, 1150, 980, 850, 1020, 970, 750, 720, 1300, 1250, 910, 880, 990],
    'average_income_level': [50000, 55000, 60000, 65000, 70000, 75000, 80000, 52000, 58000, 61000, 64000, 68000, 72000, 77000, 85000, 49000, 54000, 59000, 62000, 66000],
    'near_airport': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'price': [500000, 600000, 750000, 850000, 1000000, 1200000, 1500000, 520000, 650000, 770000, 890000, 1050000, 1250000, 1550000, 1700000, 450000, 580000, 720000, 860000, 1020000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df.drop(columns=['price'])
y = df['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
