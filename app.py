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

# defining paths to plotly graphs

@app.route('/plots/Multi_linear/Andhra Pradesh_linear.html')
def g1():
    return render_template('plots/Multi_linear/Andhra Pradesh_linear.html')
    
    @app.route('/plots/Multi_linear/Arunachal Pradesh_linear.html')
def g2():
    return render_template('plots/Multi_linear/Arunachal Pradesh_linear.html')
    
    @app.route('/plots/Multi_linear/Assam_linear.html')
def g3():
    return render_template('plots/Multi_linear/Assam_linear.html')
    
    @app.route('/plots/Multi_linear/Bihar_linear.html')
def g4():
    return render_template('plots/Multi_linear/Bihar_linear.html')
    
    @app.route('/plots/Multi_linear/Chhatisgarh_linear.html')
def g5():
    return render_template('plots/Multi_linear/Chhatisgarh_linear.html')
    
    @app.route('/plots/Multi_linear/Goa_linear.html')
def g6():
    return render_template('plots/Multi_linear/Goa_linear.html')
    
    @app.route('/plots/Multi_linear/Gujrat_linear.html')
def g7():
    return render_template('plots/Multi_linear/Gujrat_linear.html')
    
      @app.route('/plots/Multi_linear/Haryana_linear.html')
def g8():
    return render_template('plots/Multi_linear/Haryana_linear.html')
    
      @app.route('/plots/Multi_linear/Himachal Pradesh_linear.html')
def g9():
    return render_template('plots/Multi_linear/Himachal Pradesh_linear.html')
    
    @app.route('/plots/Multi_linear/Jammu & Kashmir_linear.html')
def g10():
    return render_template('plots/Multi_linear/Jammu & Kashmir_linear.html')
    
    @app.route('/plots/Multi_linear/Jharkhand_linear.html')
def g11():
    return render_template('plots/Multi_linear/Jharkhand_linear.html')
    
     @app.route('/plots/Multi_linear/Karnataka_linear.html')
def g12():
    return render_template('plots/Multi_linear/Karnataka_linear.html')
    
      @app.route('/plots/Multi_linear/Kerala_linear.html')
def g13():
    return render_template('plots/Multi_linear/kerala_linear.html')
    
      @app.route('/plots/Multi_linear/Madhya Pradesh_linear.html')
def g14():
    return render_template('plots/Multi_linear/Madhya Pradesh_linear.html')
    
      @app.route('/plots/Multi_linear/Maharastra_linear.html')
def g15():
    return render_template('plots/Multi_linear/Maharashtra_linear.html')
    
    @app.route('/plots/Multi_linear/Manipur_linear.html')
def g16():
    return render_template('plots/Multi_linear/Manipur_linear.html')
    
      @app.route('/plots/Multi_linear/Meghalaya_linear.html')
def g17():
    return render_template('plots/Multi_linear/Meghalaya_linear.html')
    
     @app.route('/plots/Multi_linear/Mizoram_linear.html')
def g18():
    return render_template('plots/Multi_linear/Mizoram_linear.html')
    
      @app.route('/plots/Multi_linear/Nagaland_linear.html')
def g19():
    return render_template('plots/Multi_linear/Nagaland_linear.html')
    
      @app.route('/plots/Multi_linear/Odisha_linear.html')
def g20():
    return render_template('plots/Multi_linear/Odisha_linear.html')
    
     @app.route('/plots/Multi_linear/Punjab_linear.html')
def g21():
    return render_template('plots/Multi_linear/Punjab_linear.html')
    
     @app.route('/plots/Multi_linear/Sikkim_linear.html')
def g22():
    return render_template('plots/Multi_linear/Sikkim_linear.html')
    
     @app.route('/plots/Multi_linear/Tamil Nadu_linear.html')
def g23():
    return render_template('plots/Multi_linear/Tamil Nadu_linear.html')
    
     @app.route('/plots/Multi_linear/Telangana_linear.html')
def g24():
    return render_template('plots/Multi_linear/Telangana_linear.html')
    
     @app.route('/plots/Multi_linear/Tripura_linear.html')
def g25():
    return render_template('plots/Multi_linear/Tripura_linear.html')
    
     @app.route('/plots/Multi_linear/Uttar Pradesh_linear.html')
def g26():
    return render_template('plots/Multi_linear/Uttar Pradesh_linear.html')
    
     @app.route('/plots/Multi_linear/Uttaranchal_linear.html')
def g27():
    return render_template('plots/Multi_linear/Uttaranchal_linear.html')
    
     @app.route('/plots/Multi_linear/West Bengal_linear.html')
def g28():
    return render_template('plots/Multi_linear/West Bengal_linear.html')
    
     @app.route('/plots/Multi_linear/A & N Islands_linear.html')
def g29():
    return render_template('plots/Multi_linear/A & N Islands_linear.html')
    
     @app.route('/plots/Multi_linear/Chandigarh_linear.html')
def g30():
    return render_template('plots/Multi_linear/Chandigarh_linear.html')
    
     @app.route('/plots/Multi_linear/D & N Haveli and Daman & Diu_linear.html')
def g31():
    return render_template('plots/Multi_linear/D & N Haveli and Daman & Diu_linear.html')

 @app.route('/plots/Multi_linear/Delhi_linear.html')
def g32():
    return render_template('plots/Multi_linear/Delhi_linear.html')
    
     @app.route('/plots/Multi_linear/Lakshadweep_linear.html')
def g33():
    return render_template('plots/Multi_linear/Lakshadweep_linear.html')
    
     @app.route('/plots/Multi_linear/Puducherry_linear.html')
def g34():
    return render_template('plots/Multi_linear/Pudducherry_linear.html')
    
     @app.route('/plots/Multi_linear/Rajasthan_linear.html')
def g35():
    return render_template('plots/Multi_linear/Rajasthan_linear.html')
    
     @app.route('/plots/Multi_linear/Assam_linear.html')
def g36():
    return render_template('plots/Multi_linear/Assam_linear.html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
if __name__ == "__main__":
    app.run(debug=True)
