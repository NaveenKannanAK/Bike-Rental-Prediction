# 🚲 Bike Rental Demand Prediction

**Predict bike rental demand using Machine Learning and XGBoost.**

Mithivandi is a machine learning web application that predicts the daily number of bike rentals based on environmental, seasonal, and calendar-related factors.

## 🎯 Project Objectives

- Analyze historical bike rental data.
- Identify factors influencing bike rental demand.
- Perform data preprocessing and exploratory data analysis.
- Compare multiple machine learning algorithms.
- Develop a prediction model using XGBoost.
- Deploy the trained model through a Flask web application.

## 📊 Dataset

The project uses the Bike Sharing Dataset, including:

- `day.csv` – Daily bike rental records.
- `hour.csv` – Hourly bike rental records.

The daily dataset contains 731 records and 16 columns.

**Target variable:** `cnt` – Total daily bike rentals.

The `casual` and `registered` columns were excluded from model inputs because they directly contribute to the target variable.

## ⚙️ Machine Learning Workflow

1. Data loading and inspection
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Feature selection
5. Train-test splitting
6. Model building and comparison
7. Hyperparameter tuning
8. Final model selection
9. Model serialization using Joblib
10. Flask web application development

## 🤖 Models Evaluated

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor

**Selected model:** Tuned XGBoost Regressor

### Model Performance

| Metric | Test Result |
|---|---:|
| MAE | 782.00 |
| RMSE | 965.34 |
| R² Score | 0.7348 |

These results represent the held-out test evaluation used for model comparison.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Flask
- HTML
- CSS
- JavaScript
- Git and GitHub

## 📁 Project Structure

```text
Bike_Rental_Prediction/
│
├── app.py
├── bike_rental_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/NaveenKannanAK/Bike-Rental-Prediction.git
```

### 2. Navigate into the project

```bash
cd Bike-Rental-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the Flask application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 🌐 Web Application

**Mithivandi** provides an interactive interface where users can enter seasonal, weather, and calendar information to predict daily bike rental demand.

## 👨‍💻 Author

**Naveen AK**

- GitHub: [NaveenKannanAK](https://github.com/NaveenKannanAK)

---

*Developed as a Data Science and Machine Learning project.*
