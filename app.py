#importing the required libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#creation of the Flask Application named as "app"
app = Flask(__name__)

#loading the pickle files of the five models which are used in read binary mode
model1 = pickle.load(open('car_price.pkl', 'rb'))
model2 = pickle.load(open('laptop_price.pkl', 'rb'))
model3 = pickle.load(open('bitcoin_price.pkl', 'rb'))
model4 = pickle.load(open('gold_price.pkl', 'rb'))
model5 = pickle.load(open('house_price.pkl', 'rb'))

@app.route('/home')
@app.route('/')
def home():
    #renders the home page template 
    return render_template('index.html')