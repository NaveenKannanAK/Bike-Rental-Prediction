
from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Get the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
MODEL_PATH = os.path.join(BASE_DIR, "bike_rental_model.pkl")
model = joblib.load(MODEL_PATH)

# Features must follow the same order used during model training
FEATURE_COLUMNS = [
    'season',
    'yr',
    'mnth',
    'holiday',
    'weekday',
    'workingday',
    'weathersit',
    'temp',
    'atemp',
    'hum',
    'windspeed'
]


@app.route('/')
def home():
    return render_template(
        'index.html',
        prediction=None,
        error=None
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the HTML form
        input_data = {
            'season': int(request.form['season']),
            'yr': int(request.form['yr']),
            'mnth': int(request.form['mnth']),
            'holiday': int(request.form['holiday']),
            'weekday': int(request.form['weekday']),
            'workingday': int(request.form['workingday']),
            'weathersit': int(request.form['weathersit']),
            'temp': float(request.form['temp']),
            'atemp': float(request.form['atemp']),
            'hum': float(request.form['hum']),
            'windspeed': float(request.form['windspeed'])
        }

        # Create a DataFrame with the correct feature order
        input_df = pd.DataFrame(
            [input_data],
            columns=FEATURE_COLUMNS
        )

        # Validate normalized environmental values
        for column in ['temp', 'atemp', 'hum', 'windspeed']:
            if not 0 <= input_df.loc[0, column] <= 1:
                raise ValueError(
                    f"{column} must be between 0 and 1."
                )

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Rental count cannot be negative
        prediction = max(0, round(float(prediction)))

        return render_template(
            'index.html',
            prediction=prediction,
            error=None
        )

    except (ValueError, KeyError) as e:
        return render_template(
            'index.html',
            prediction=None,
            error=f"Please check your input values: {e}"
        )

    except Exception:
        return render_template(
            'index.html',
            prediction=None,
            error="Prediction failed. Please check the inputs and try again."
        )


# Run Flask locally
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
