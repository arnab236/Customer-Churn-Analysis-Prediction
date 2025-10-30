# 🧠 Customer Churn Analysis & Prediction

Predict customer churn using machine learning models and visualize insights from customer data.
This project includes a data analysis notebook and a Streamlit web app for real-time churn prediction.

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Model Overview](#model-overview)
7. [Dependencies](#dependencies)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)

---

## 🧩 Introduction

Customer churn occurs when clients stop doing business with a company.
This project applies machine learning techniques to analyze churn patterns and predict whether a customer is likely to leave based on their attributes (e.g., age, gender, tenure, and monthly charges).

The project includes:

* A **Jupyter Notebook (`notebook.ipynb`)** for data analysis, preprocessing, and model training.
* A **Streamlit App (`app.py`)** for making live churn predictions.

---

## 📁 Project Structure

```
├── app.py                # Streamlit web application for churn prediction
├── notebook.ipynb        # Data analysis and model training notebook
├── model.pkl             # Trained machine learning model
├── scaler.pkl            # Feature scaler used for preprocessing
├── requirements.txt      # List of dependencies (to be generated)
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arnab236/Customer-Churn-Analysis-Prediction.git
   cd Customer-Churn-Analysis-Prediction
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # (Mac/Linux)
   venv\Scripts\activate       # (Windows)
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

Once running, the app will open in your default browser.
You’ll be prompted to input customer details such as:

* **Age**
* **Gender** (0 = Male, 1 = Female)
* **Tenure**
* **Monthly Charges**

The app will display whether the customer is **likely to churn** or **not**.

---

## ✨ Features

* Interactive web interface built with **Streamlit**
* Machine learning model trained for churn prediction
* Feature scaling and consistent preprocessing pipeline
* Clear data visualization and analysis in Jupyter Notebook
* Modular, easy-to-extend codebase

---

## 🧠 Model Overview

* **Input Features:** `Age`, `Gender`, `Tenure`, `MonthlyCharges`
* **Model Artifacts:**

  * `model.pkl` → Trained classifier (likely Logistic Regression or RandomForest)
  * `scaler.pkl` → Scikit-learn StandardScaler for consistent feature scaling
* **Output:** Binary churn prediction (`1` = Yes, `0` = No)

---

## 📦 Dependencies

The key dependencies (from your app and notebook) include:

```txt
streamlit
numpy
pandas
matplotlib
scikit-learn
joblib
```

You can generate a full list using:

```bash
pip freeze > requirements.txt
```

---

## 🧰 Troubleshooting

* **App not loading model/scaler:**
  Ensure `model.pkl` and `scaler.pkl` are in the same directory as `app.py`.
* **Streamlit not found:**
  Run `pip install streamlit`.
* **Model mismatch error:**
  Retrain the model and regenerate `model.pkl` and `scaler.pkl` from the notebook.

---

## 📜 License

This project is licensed under the **MIT License** 

---

