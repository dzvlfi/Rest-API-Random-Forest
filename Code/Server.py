
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
import numpy as np
#import pickle
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('/home/dzvlfi/mysite/RF.pkl','rb'))

@app.route('/')
def hello_world():
    return 'Hello from Jul The Saviour!'

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([np.array([data["LIMIT_BAL"],data["EDUCATION"],data["SEX"],data["AGE"],data["PAY_1"],data["PAY_2"],data["PAY_3"]])])

    # Take the first value of prediction
    output = int(prediction[0])
    out =  'Pass' if output==1 else 'Not Pass'

    return jsonify(out)

@app.route('/predicts',methods=['POST'])
def predicts():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []

    # Make prediction using model loaded from disk as per the data.
    for data in datas:
        prediction = model.predict([np.array([data["LIMIT_BAL"],data["EDUCATION"],data["SEX"],data["AGE"],data["PAY_1"],data["PAY_2"],data["PAY_3"]])])

        # Take the first value of prediction
        output = int(prediction[0])
        out =  'Pass' if output==1 else 'Not Pass'
        pred.append(out)

    return jsonify(pred)
