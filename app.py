from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from sklearn.externals import joblib
import numpy as np
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':

        regressor = joblib.load("linear_regression_model.pkl")

        data = dict(request.form.items())

        years_of_experience = np.array(float(data["YearsExperience"])).reshape(-1,1)

        prediction = regressor.predict(years_of_experience)

    return render_template("predicted.html", prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
