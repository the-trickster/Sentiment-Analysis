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
    data = request.form.get("first_name")
    print(data)
    prediction = model.predict(data)
    output = str(prediction[0])
    
    if output == 0:
        return render_template('index.html',pred='Negative Sentiment')
    elif ouput ==1:
        return render_template('index.html',pred='Positive Sentiment')
    else:
        return render_template('index.html',pred='Neutral Sentiment')

if __name__ == '__main__':
    app.run(debug=True)
