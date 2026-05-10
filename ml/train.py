import pandas as pd
import numpy as np
import joblib
import json
import os
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

def train():
    # ── 1. Load cleaned data ──
    print("📂 Loading cleaned data...")
    df = pd.read_csv("data/cleaned/cleaned_movie_data.csv")
    print(f"✅ Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # ── 2. Split features and target ──
    X = df.drop('revenue', axis=1)
    y = df['revenue']
    print(f"✅ Features: {X.shape[1]} columns")

    # ── 3. Train test split ──
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"✅ Train rows: {X_train.shape[0]}")
    print(f"✅ Test rows : {X_test.shape[0]}")

    # ── 4. Scale features for Linear Regression ──
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    # ── 5. Train Linear Regression ──
    print("\n🔄 Training Linear Regression...")
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    y_pred_lr = lr.predict(X_test_scaled)
    r2_lr  = r2_score(y_test, y_pred_lr)
    mae_lr = np.mean(np.abs(np.expm1(y_test) - np.expm1(y_pred_lr)))
    print(f"✅ Linear Regression → R²: {r2_lr:.4f} | MAE: ${mae_lr:,.2f}")

    # ── 6. Train Random Forest ──
    print("\n🔄 Training Random Forest (takes 2-5 mins)...")
    rf = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    r2_rf  = r2_score(y_test, y_pred_rf)
    mae_rf = np.mean(np.abs(np.expm1(y_test) - np.expm1(y_pred_rf)))
    print(f"✅ Random Forest     → R²: {r2_rf:.4f} | MAE: ${mae_rf:,.2f}")

    # ── 7. Save everything ──
    print("\n💾 Saving models...")
    os.makedirs("ml/saved_model", exist_ok=True)

    joblib.dump(lr,     "ml/saved_model/linear_regression.pkl")
    joblib.dump(rf,     "ml/saved_model/random_forest.pkl")
    joblib.dump(scaler, "ml/saved_model/scaler.pkl")

    with open("ml/saved_model/feature_columns.json", "w") as f:
        json.dump(X_train.columns.tolist(), f)

    print("✅ linear_regression.pkl saved")
    print("✅ random_forest.pkl saved")
    print("✅ scaler.pkl saved")
    print("✅ feature_columns.json saved")

    # ── 8. Final summary ──
    print("\n" + "="*45)
    print("TRAINING SUMMARY")
    print("="*45)
    print(f"Linear Regression  R²  : {r2_lr:.4f}")
    print(f"Random Forest      R²  : {r2_rf:.4f}")
    print(f"Linear Regression  MAE : ${mae_lr:,.2f}")
    print(f"Random Forest      MAE : ${mae_rf:,.2f}")
    print("="*45)

if __name__ == "__main__":
    train()