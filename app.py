#scikit-learn==0.22.1
from flask import Flask,request, url_for, redirect, render_template
import joblib
import json
import numpy as np

app = Flask(__name__)
model = joblib.load(r'Sentiment')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def prediction():
    data = request.get_json()
    values = data['values']
    prediction = model.predict(data)
    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
