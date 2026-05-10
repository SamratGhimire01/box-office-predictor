import joblib
import numpy as np
import json
import pandas as pd

# ── Load models once at startup ──
lr_model = joblib.load("ml/saved_model/linear_regression.pkl")
rf_model = joblib.load("ml/saved_model/random_forest.pkl")
scaler   = joblib.load("ml/saved_model/scaler.pkl")

with open("ml/saved_model/feature_columns.json") as f:
    feature_columns = json.load(f)


def predict_linear_regression(features: dict) -> float:
    """
    Predict revenue using Linear Regression.
    Args:
        features: dictionary of movie features
    Returns:
        predicted revenue in USD
    """
    if not features:
        raise ValueError("Features dictionary cannot be empty")

    input_data = pd.DataFrame(
        [[features.get(col, 0) for col in feature_columns]],
        columns=feature_columns
    )
    input_scaled   = scaler.transform(input_data)
    log_prediction = lr_model.predict(input_scaled)[0]
    return float(np.expm1(log_prediction))


def predict_random_forest(features: dict) -> float:
    """
    Predict revenue using Random Forest.
    Args:
        features: dictionary of movie features
    Returns:
        predicted revenue in USD
    """
    if not features:
        raise ValueError("Features dictionary cannot be empty")

    input_data = pd.DataFrame(
        [[features.get(col, 0) for col in feature_columns]],
        columns=feature_columns
    )
    log_prediction = rf_model.predict(input_data)[0]
    return float(np.expm1(log_prediction))
