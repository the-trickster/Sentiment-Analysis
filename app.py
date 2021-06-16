#scikit-learn==0.22.1
from flask import Flask,request, url_for, redirect, render_template
import joblib
import json
import numpy as np
from sklearn import *

app = Flask(__name__)
model = joblib.load(r'Sentiment')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def prediction():
    data = request.form['first_name']
    prediction = model.predict([data])

    if prediction == 0:
        return render_template('index.html',pred='Negative Sentiment')
    elif prediction == 0:
        return render_template('index.html',pred='Positive Sentiment')
    else:
        return render_template('index.html',pred='Neutral Sentiment')

if __name__ == '__main__':
    app.run(debug=True)
