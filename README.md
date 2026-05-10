---
title: Box Office Revenue Predictor
emoji: 🎬
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
---

# 🎬 Box Office Revenue Predictor

<p align="center">
  <b>A full-stack ML web app that predicts movie box office revenue</b><br>
  Clean • Fast • Deployed • Built from scratch
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-316192?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn">
  <img src="https://img.shields.io/badge/HuggingFace-Deployed-yellow?style=for-the-badge&logo=huggingface">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🚀 Overview

**Box Office Revenue Predictor** is a production-ready ML web application that predicts the worldwide box office revenue of a movie based on its features like budget, genre, language, season, and popularity.

The project demonstrates a full data science pipeline — from raw dirty data to a live deployed API with a frontend UI.

- 🧹 Cleaned **1.4 million rows** down to **10,324 usable rows**
- 📉 Started with **Linear Regression (R² = 0.58)**
- 📈 Improved to **Random Forest (R² = 0.67)**, reducing MAE by **$24 million**
- 🌐 Deployed live on **Hugging Face Spaces** with **Supabase PostgreSQL**

---

## ✨ Features

- ✅ Two ML models — **Linear Regression** and **Random Forest**
- ✅ Switch between models live — **auto re-predicts instantly**
- ✅ Green theme for Random Forest, Blue theme for Linear Regression
- ✅ Prediction history saved to **PostgreSQL** database
- ✅ View all past predictions with one click
- ✅ Full **FastAPI** REST backend with `/predict` and `/history` endpoints
- ✅ Log transformation applied to handle skewed revenue data
- ✅ Genre multi-label encoding, season encoding, language encoding

---

## 📸 Demo

### 🎯 Prediction UI — Random Forest (Green Theme)
![Random Forest UI](images/rf_demo.png)

### 🔵 Prediction UI — Linear Regression (Blue Theme)
![Linear Regression UI](images/lr_demo.png)

### 🗃️ Prediction History
![History](images/history_demo.png)

---

## ⚙️ Installation

```bash
git clone https://github.com/SamratGhimire01/box-office-predictor.git
cd box-office-predictor

# Create virtual environment
python3 -m venv venv

# Activate — Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

```bash
# Start PostgreSQL
sudo systemctl start postgresql

# Create database and user
sudo -u postgres psql -c "CREATE DATABASE boxoffice;"
sudo -u postgres psql -c "CREATE USER boxoffice_user WITH PASSWORD 'boxoffice123';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE boxoffice TO boxoffice_user;"
```

Create a `.env` file:
```
DATABASE_URL=postgresql://boxoffice_user:boxoffice123@localhost:5432/boxoffice
MODEL_PATH=ml/saved_model
```

---

## 🧠 ML Pipeline

### Step 1 — Data Cleaning
```bash
python data/raw/cleaning.py
```

### Step 2 — Train Both Models
```bash
python ml/train.py
```

### Step 3 — Prediction Function
```bash
python ml/predict.py
```

### Step 4 — Run the API
```bash
uvicorn app.main:app --reload
```

Open **http://localhost:8000** in your browser.

---

## 📊 Model Performance

| Model | R² Score | MAE |
|---|---|---|
| Linear Regression | 0.5823 | $64,857,742 |
| Random Forest | 0.6691 | $40,408,542 |
| **Improvement** | **+8.68%** | **-$24M** |

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Frontend UI |
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/predict` | Predict revenue |
| GET | `/api/v1/history` | All past predictions |

### Example Request
```json
POST /api/v1/predict
{
  "model_type": "random_forest",
  "budget": 150000000,
  "runtime": 148,
  "popularity": 83.9,
  "vote_average": 8.3,
  "language_count": 2,
  "season": "Summer",
  "language": "en",
  "action": 1,
  "adventure": 1,
  "science_fiction": 1
}
```

### Example Response
```json
{
  "model_used": "random_forest",
  "predicted_revenue_usd": 521883836.87,
  "predicted_revenue_fmt": "$521,883,836.87"
}
```

---

## 🧹 Data Cleaning Story

| Step | Rows |
|---|---|
| Raw dataset | 1,420,364 |
| After removing zero budget/revenue | 17,380 |
| After removing nulls in genres/date | 13,443 |
| After removing fake low budgets (<$10K) | 10,324 |

Key transformations applied:
- **Log transformation** on budget and revenue to handle right skew
- **MultiLabelBinarizer** for genre encoding
- **One-hot encoding** for season and language
- **Top 8 languages** kept, rest grouped as `other`

---

## 📁 Project Structure

```
box-office-predictor/
├── app/
│   ├── main.py
│   ├── api/routes/
│   │   ├── predict.py
│   │   └── health.py
│   ├── core/config.py
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── crud.py
│   └── templates/
│       └── index.html
├── ml/
│   ├── train.py
│   ├── predict.py
│   └── saved_model/
│       ├── linear_regression.pkl
│       ├── random_forest.pkl
│       ├── scaler.pkl
│       └── feature_columns.json
├── data/
│   ├── raw/
│   └── cleaned/
├── images/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🎯 Why This Project Matters

This project demonstrates:
- Real-world **data cleaning** on a 1.4M row dataset
- **Iterative ML thinking** — starting simple, improving with evidence
- Full **API development** with FastAPI and PostgreSQL
- **Production deployment** on Hugging Face Spaces
- **Frontend UI** with live model switching

👉 Relevant for roles in:
- ML Engineer
- Data Scientist
- Backend Python Developer
- Full Stack ML Developer

---

## 👨‍💻 Author

**Samrat Ghimire**

🔗 GitHub: https://github.com/SamratGhimire01
🔗 LinkedIn: https://www.linkedin.com/in/samratghimire01/

<p align="center">⭐ If you like this project, consider giving it a star!</p>