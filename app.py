#scikit-learn==0.22.1
from flask import Flask,request,jsonify
import joblib
import json
import numpy as np
from sklearn import *


app = Flask(__name__)
model = joblib.load(r'Sentiment')

@app.route('/')
def hello():
    return 'hello world!'

@app.route('/predict' , methods=['POST'])
def prediction():
    data = request.get_json()
    data = data['values']
    prediction = model.predict(data)
    return str(prediction[0])
app.run(port=5001, debug=True)