# 💳 CreditGuard ML – Credit Risk Scoring System

An **industry-level Machine Learning project** that predicts **loan default risk** using **Logistic Regression**, the most widely accepted and regulatory-friendly model in banking and fintech.

This system simulates how real banks evaluate customer creditworthiness **before loan approval**, combining **machine learning, data preprocessing pipelines, and a professional Flask-based UI**.

---

## 🚀 Project Overview

**CreditGuard ML** is a full-stack ML application that:

- Predicts whether a customer is **high risk or low risk** for loan default
- Uses a **single interpretable ML model** (Logistic Regression)
- Applies **proper ML pipelines** (scaling + encoding)
- Exposes predictions through a **Flask web application**
- Presents results via a **clean, professional UI**

This project follows **real industry standards** used in financial institutions.

---

## 🎯 Why Logistic Regression?

Logistic Regression is intentionally chosen because it is:

- ✅ Used by **banks & fintech companies**
- ✅ **Highly interpretable** (required by regulators)
- ✅ Stable and explainable
- ✅ Suitable for credit risk modeling
- ✅ Audit-friendly (Basel / RBI / compliance ready)

> ⚠️ Complex black-box models are often **rejected** in finance — interpretability matters.

---

## 📊 Dataset

- **Source**: Kaggle  
- **Link**: https://www.kaggle.com/datasets/laotse/credit-risk-dataset  

### Dataset Description

The dataset contains **customer demographic, employment, and credit history data**, used to predict loan default risk.

| Column Name | Description |
|------------|------------|
| person_age | Age of the applicant |
| person_income | Annual income |
| person_emp_length | Employment length (years) |
| person_home_ownership | Home ownership status |
| loan_intent | Purpose of loan |
| loan_grade | Loan grade assigned by lender |
| loan_amnt | Loan amount |
| loan_int_rate | Interest rate |
| loan_percent_income | Loan amount as % of income |
| cb_person_default_on_file | Previous default history |
| cb_person_cred_hist_length | Credit history length |
| loan_status | **Target variable (0 = No Default, 1 = Default)** |

> ✅ All missing values were handled before training (median-based imputation).

---

## 🧠 Machine Learning Pipeline

The project uses a **clean and beginner-friendly ML pipeline**, similar to industry workflows:

