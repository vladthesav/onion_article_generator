from flask import Flask, jsonify,request, after_this_request
from model import predict
import numpy as np
import json
import os

app = Flask(__name__)

@app.route('/')
def test():
    return jsonify({'it':'works'})

@app.route('/predict',methods = ['POST'])
def pred():
    #get input text  from user
    data = request.get_json()
    print(data)
    text = data['text']

    #run through GPT2
    prediction = predict(text, len_sequence=150)
    prediction = str(prediction).replace("<|endoftext|>", "")
    return jsonify({'output':prediction.decode("utf-8")})

if __name__ == '__main__':
    app.run(debug=True, port=3500,host='0.0.0.0')