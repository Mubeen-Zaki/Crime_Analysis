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

#home:
@app.route('/index.html')
def index():
    return render_template('index.html')

#kmeans:
@app.route('/K-Means.html',methods=['POST'])
def KMeansclu():
    features = [x for x in request.form.values()]
    df = pd.read_csv("Datasets/01_District_wise_crimes_committed_IPC_2001_2012.csv")
    df.drop(["CULPABLE HOMICIDE NOT AMOUNTING TO MURDER", "CUSTODIAL RAPE", "OTHER RAPE", "KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS", "KIDNAPPING AND ABDUCTION OF OTHERS", "PREPARATION AND ASSEMBLY FOR DACOITY", "BURGLARY", "AUTO THEFT", "OTHER THEFT", "CRIMINAL BREACH OF TRUST", "CHEATING", "COUNTERFIETING", "ARSON", "ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY", "INSULT TO MODESTY OF WOMEN", "CRUELTY BY HUSBAND OR HIS RELATIVES", "IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES", "CAUSING DEATH BY NEGLIGENCE", "OTHER IPC CRIMES","TOTAL IPC CRIMES","RIOTS","DOWRY DEATHS"], axis=1, inplace=True)
    df = df.loc[df['DISTRICT']!='TOTAL']
    df2 = pd.DataFrame([features], columns=["STATE/UT","DISTRICT","YEAR","MURDER","ATTEMPT TO MURDER","RAPE","KIDNAPPING & ABDUCTION","DACOITY","ROBBERY","THEFT","HURT/GREVIOUS HURT"])
    df = pd.concat([df2, df])

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df["STATE/UT"]=le.fit_transform(df["STATE/UT"].astype("str"))
    df["STATE/UT"].value_counts()

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df["DISTRICT"]=le.fit_transform(df["DISTRICT"].astype("str"))
    df["DISTRICT"].value_counts()
    #Prediction:
    final_features = np.array(df.head(1))
    y_pred = kmeanclus.predict(final_features)
    if y_pred[0] == 0:         
        label="Moderate Crime Rate Area"
    elif y_pred[0] == 1:
        label="High Crime Rate Area"
    elif y_pred[0] == 2:
        label = "Low Crime Rate Area"
    return render_template('K-Means.html',prediction_text= label)

#K-Prototypes:
@app.route('/K-Proto.html',methods=['POST'])
def KProtoclu():
    features = [[x for x in request.form.values()]]
    features = pd.DataFrame(features)
    features = features.values
    y_pred = kprotoclus.predict(features, categorical=[0,1,2])
    if y_pred[0] == 0:         
        label = "Moderate Crime Rate Area"
    elif y_pred[0] == 1:
        label="Low Crime Rate Area"
    elif y_pred[0] == 2:
        label = "High Crime Rate Area"
    return render_template('K-Proto.html',prediction_text= label)

#RandomForest:
@app.route('/Randomforestclassifier.html',methods=['POST'])
def randomfrstcls():
    features = [x for x in request.form.values()]
    df = pd.read_csv("Datasets/01_District_wise_crimes_committed_IPC_2001_2012.csv")
    df.drop(["CULPABLE HOMICIDE NOT AMOUNTING TO MURDER", "CUSTODIAL RAPE", "OTHER RAPE", "KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS", "KIDNAPPING AND ABDUCTION OF OTHERS", "PREPARATION AND ASSEMBLY FOR DACOITY", "BURGLARY", "AUTO THEFT", "OTHER THEFT", "CRIMINAL BREACH OF TRUST", "CHEATING", "COUNTERFIETING", "ARSON", "ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY", "INSULT TO MODESTY OF WOMEN", "CRUELTY BY HUSBAND OR HIS RELATIVES", "IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES", "CAUSING DEATH BY NEGLIGENCE", "OTHER IPC CRIMES","TOTAL IPC CRIMES","RIOTS","DOWRY DEATHS"], axis=1, inplace=True)
    df = df.loc[df['DISTRICT']!='TOTAL']
    df2 = pd.DataFrame([features], columns=["STATE/UT","DISTRICT","YEAR","MURDER","ATTEMPT TO MURDER","RAPE","KIDNAPPING & ABDUCTION","DACOITY","ROBBERY","THEFT","HURT/GREVIOUS HURT"])
    df = pd.concat([df2, df])

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df["STATE/UT"]=le.fit_transform(df["STATE/UT"].astype("str"))
    df["STATE/UT"].value_counts()

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df["DISTRICT"]=le.fit_transform(df["DISTRICT"].astype("str"))
    df["DISTRICT"].value_counts()

    #Prediction:
    features = pd.DataFrame(df.head(1))
    y_pred = rdcls.predict(features)
    if y_pred[0] == 0:         
        label="Moderate Crime Rate Area"
    elif y_pred[0] == 1:
        label="Low Crime Rate Area"
    elif y_pred[0] == 2:
        label = "High Crime Rate Area"
    return render_template('Randomforestclassifier.html',prediction_text = label)

#LinearRegression:
@app.route('/linearregression.html',methods=["POST"])
def linearreg():
    test = pd.DataFrame([[x for x in request.form.values()]])
    y_pred = mlr.predict(test)
    return render_template('linearregression.html',y_pred)

# time series forecasting pages missing for crime rate, ipc
@app.route('/timeseries.html')
def timeseriesipc():
    return render_template('timeseries.html')

@app.route('/timeseries1.html')
def timeseriescr():
    return render_template('timeseries1.html')

#Google charts:
@app.route('/Analysis.html')
def analysis():
    return render_template('Analysis.html') #google charts

#Plotly charts:
@app.route('/Analysis2.html')
def analysis2():
    return render_template('Analysis2.html') #plotly charts

#Geospatial analysis:
@app.route('/Analysis3(maps).html')
def analysis3():
    return render_template('Analysis3(maps).html') #geospatial analysis


# src links not working

# datasets pages missing

# webscrapped data plotted on heat maps with rss feed

# heat maps / crime locator / nothing
  
if __name__ == "__main__":
    app.run(debug=True)