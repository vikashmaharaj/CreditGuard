from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("credit_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "person_age": int(request.form["person_age"]),
        "person_income": int(request.form["person_income"]),
        "person_emp_length": float(request.form["person_emp_length"]),
        "loan_amnt": int(request.form["loan_amnt"]),
        "loan_int_rate": float(request.form["loan_int_rate"]),
        "loan_percent_income": float(request.form["loan_percent_income"]),
        "cb_person_cred_hist_length": int(request.form["cb_person_cred_hist_length"]),
        "person_home_ownership": request.form["person_home_ownership"],
        "loan_intent": request.form["loan_intent"],
        "loan_grade": request.form["loan_grade"],
        "cb_person_default_on_file": request.form["cb_person_default_on_file"]
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    result = "✅ LOW CREDIT RISK" if prediction == 0 else "❌ HIGH CREDIT RISK"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
