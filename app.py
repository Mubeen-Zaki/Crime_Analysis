from flask import Flask, render_template, request, url_for, Markup, jsonify
import pickle
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
import joblib

#Initialize the flask App
app = Flask(__name__)

#Deserializing ml models
kmeanclus = pickle.load(open('./Prediction/kmean.pkl','rb'))
kprotoclus = joblib.load('./Prediction/kproto.pkl')
rdcls = joblib.load('./Prediction/cls.pkl')
mlr = joblib.load('./Prediction/crime_factors.pkl')

@app.route('/')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/clusterfeed.html')
def clusterfeed():
    return render_template('clusterfeed.html')

@app.route('/K-Means.html')
def KMeans():
    return render_template('K-Means.html') # Remove dataset from this page

# Kproto type page missing
# all the pages are not linked to each other

@app.route('/K-Means.html')
def kmeansclu():
    return render_template('K-Means.html')

@app.route('/Randomforestclassifier.html')
def randomfrstcls():
    return render_template('Randomforestclassifier.html')

@app.route('/linearregression.html')
def linearreg():
    return render_template('linearregression.html')

# time series forecasting pages missing for crime rate, ipc
# hover opt for 2 pages

@app.route('/Analysis.html')
def analysis():
    return render_template('Analysis.html') #google charts

@app.route('/Analysis2.html')
def analysis2():
    return render_template('Analysis2.html') #plotly charts
# src links not working 

@app.route('/Analysis3(maps).html')
def analysis3():
    return render_template('Analysis3(maps).html') #geospatial analysis
# src links not working

# datasets pages missing

# webscrapped data plotted on heat maps with rss feed

# heat maps / crime locator / nothing
  
if __name__ == "__main__":
    app.run(debug=True)