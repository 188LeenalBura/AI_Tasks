import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
from flask import Flask, request, jsonify, render_template

# Step 1: Load dataset
data = pd.read_csv('housing_prices.csv')

# Step 2: Prepare the dataset with the new features
X = data[['near_airport', 'bedrooms', 'bathrooms', 'floor_number', 'age_of_house', 'population_density', 'average_income_level']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Root Mean Squared Error: {rmse}')

# Step 5: Export the model
with open('regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Step 6: Create a Flask API
app = Flask(__name__)

# Load the trained model
with open('regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the features from the form
        features = [
            float(request.form['near_airport']),
            int(request.form['bedrooms']),
            int(request.form['bathrooms']),
            int(request.form['floor_number']),
            int(request.form['age_of_house']),
            float(request.form['population_density']),
            float(request.form['average_income_level']),
        ]
        # Make a prediction
        prediction = loaded_model.predict([features])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Predicted Price: ${output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)

# Step 7: Frontend code (HTML)
frontend_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>House Price Prediction</title>
</head>
<body>
    <h1>House Price Prediction</h1>
    <form action="/predict" method="post">
        <label for="near_airport">Near Airport (0 for No, 1 for Yes):</label>
        <input type="text" id="near_airport" name="near_airport"><br><br>
        <label for="bedrooms">Bedrooms:</label>
        <input type="text" id="bedrooms" name="bedrooms"><br><br>
        <label for="bathrooms">Bathrooms:</label>
        <input type="text" id="bathrooms" name="bathrooms"><br><br>
        <label for="floor_number">Number of Floors:</label>
        <input type="text" id="floor_number" name="floor_number"><br><br>
        <label for="age_of_house">Age of House (in years):</label>
        <input type="text" id="age_of_house" name="age_of_house"><br><br>
        <label for="population_density">Population Density (per sq. km):</label>
        <input type="text" id="population_density" name="population_density"><br><br>
        <label for="average_income_level">Average Income Level (INR):</label>
        <input type="text" id="average_income_level" name="average_income_level"><br><br>
        <input type="submit" value="Predict">
    </form>
    <h2>{{ prediction_text }}</h2>
</body>
</html>
'''

with open('templates/index.html', 'w') as f:
    f.write(frontend_code)
