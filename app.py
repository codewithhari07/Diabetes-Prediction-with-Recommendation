import streamlit as st
from flask import Flask, request, render_template
import numpy as np
import pickle
from utils.recommend import get_recommendation
import pandas as pd

app = Flask(__name__)

# Load files

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
threshold = pickle.load(open("threshold.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():

    features = [float(x) for x in request.form.values()]

    # Reshape and Scale
    columns = ["Pregnancies","Glucose","BloodPressure","SkinThickness",
           "Insulin","BMI","DiabetesPedigreeFunction","Age"]

    input_df = pd.DataFrame([features], columns=columns)

    input_scale = scaler.transform(input_df)

    # Get probability
    prob = model.predict_proba(input_scale)[0][1]
    
    # Apply threshold
    prediction = 1 if prob > threshold else 0

     # convert to dictionary for recommendation
    keys = ["Pregnancies","Glucose","BloodPressure","SkinThickness",
            "Insulin","BMI","DiabetesPedigreeFunction","Age"]

    input_dict = dict(zip(keys, features))

    # get recommendation
    rec = get_recommendation(input_dict)

    #Result
    if prediction == 1:
        result = "High Risk of Diabetes" 
    else:
        result = "Low Risk of Diabetes" 

    return render_template("index.html", prediction = result, probability = round(prob, 2), recommendation = rec)

if __name__ == "__main__":
    app.run(debug= True, use_reloader = True)