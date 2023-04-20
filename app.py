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

@app.route('/plots/Stacked_Bar_Charts/Andhra Pradesh_stbar.html')
def g37():
    return render_template('plots/Stacked_Bar_Charts/Andhra Pradesh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Arunachal Pradesh_stbar.html')
def g38():
    return render_template('plots/Stacked_Bar_Charts/Arunachal Pradesh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Assam_stbar.html')
def g39():
    return render_template('plots/Stacked_Bar_Charts/Assam_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Bihar_stbar.html')
def g40():
    return render_template('plots/Stacked_Bar_Charts/Bihar_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Chhatisgarh_stbar.html')
def g41():
    return render_template('plots/Stacked_Bar_Charts/Chhatisgarh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Goa_stbar.html')
def g42():
    return render_template('plots/Stacked_Bar_Charts/Goa_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Gujrat_stbar.html')
def g43():
    return render_template('plots/Stacked_Bar_Charts/Gujrat_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Haryana_stbar.html')
def g44():
    return render_template('plots/Stacked_Bar_Charts/Haryana_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Himachal Pradesh_stbar.html')
def g45():
    return render_template('plots/Stacked_Bar_Charts/Himachal Pradesh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Jammu & Kashmir_stbar.html')
def g46():
    return render_template('plots/Stacked_Bar_Charts/Jammu & Kashmir_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Jharkhand_stbar.html')
def g47():
    return render_template('plots/Stacked_Bar_Charts/Jharkhand_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Karnataka_stbar.html')
def g48():
    return render_template('plots/Stacked_Bar_Charts/Karnataka_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Kerala_stbar.html')
def g49():
    return render_template('plots/Stacked_Bar_Charts/kerala_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Madhya Pradesh_stbar.html')
def g50():
    return render_template('plots/Stacked_Bar_Charts/Madhya Pradesh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Maharastra_stbar.html')
def g51():
    return render_template('plots/Stacked_Bar_Charts/Maharashtra_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Manipur_stbar.html')
def g52():
    return render_template('plots/Stacked_Bar_Charts/Manipur_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Meghalaya_stbar.html')
def g53():
    return render_template('plots/Stacked_Bar_Charts/Meghalaya_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Mizoram_stbar.html')
def g54():
    return render_template('plots/Stacked_Bar_Charts/Mizoram_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Nagaland_stbar.html')
def g55():
    return render_template('plots/Stacked_Bar_Charts/Nagaland_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Odisha_stbar.html')
def g56():
    return render_template('plots/Stacked_Bar_Charts/Odisha_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Punjab_.html')
def g57():
    return render_template('plots/Stacked_Bar_Charts/Punjab_.html')
    
@app.route('/plots/Stacked_Bar_Charts/Sikkim_stbar.html')
def g58():
    return render_template('plots/Stacked_Bar_Charts/Sikkim_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Tamil Nadu_stbar.html')
def g59():
    return render_template('plots/Stacked_Bar_Charts/Tamil Nadu_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Telangana_stbar.html')
def g60():
    return render_template('plots/Stacked_Bar_Charts/Telangana_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Tripura_stbar.html')
def g61():
    return render_template('plots/Stacked_Bar_Charts/Tripura_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Uttar Pradesh_stbar.html')
def g62():
    return render_template('plots/Stacked_Bar_Charts/Uttar Pradesh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Uttaranchal_stbar.html')
def g63():
    return render_template('plots/Stacked_Bar_Charts/Uttaranchal_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/West Bengal_stbar.html')
def g64():
    return render_template('plots/Stacked_Bar_Charts/West Bengal_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/A & N Islands_stbar.html')
def g65():
    return render_template('plots/Stacked_Bar_Charts/A & N Islands_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Chandigarh_stbar.html')
def g66():
    return render_template('plots/Stacked_Bar_Charts/Chandigarh_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/D & N Haveli and Daman & Diu_stbar.html')
def g67():
    return render_template('plots/Stacked_Bar_Charts/D & N Haveli and Daman & Diu_stbar.html')

@app.route('/plots/Stacked_Bar_Charts/Delhi_stbar.html')
def g68():
    return render_template('plots/Stacked_Bar_Charts/Delhi_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Lakshadweep_stbar.html')
def g69():
    return render_template('plots/Stacked_Bar_Charts/Lakshadweep_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Puducherry_stbar.html')
def g70():
    return render_template('plots/Stacked_Bar_Charts/Pudducherry_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Rajasthan_stbar.html')
def g71():
    return render_template('plots/Stacked_Bar_Charts/Rajasthan_stbar.html')
    
@app.route('/plots/Stacked_Bar_Charts/Assam_stbar.html')
def g72():
    return render_template('plots/Stacked_Bar_Charts/Assam_stbar.html')

@app.route('/plots/Grouped_Bar_Charts/Andhra Pradesh_grbar.html')
def g73():
    return render_template('plots/Grouped_Bar_Charts/Andhra Pradesh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Arunachal Pradesh_grbar.html')
def g74():
    return render_template('plots/Grouped_Bar_Charts/Arunachal Pradesh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Assam_grbar.html')
def g75():
    return render_template('plots/Grouped_Bar_Charts/Assam_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Bihar_grbar.html')
def g76():
    return render_template('plots/Grouped_Bar_Charts/Bihar_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Chhatisgarh_grbar.html')
def g77():
    return render_template('plots/Grouped_Bar_Charts/Chhatisgarh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Goa_grbar.html')
def g78():
    return render_template('plots/Grouped_Bar_Charts/Goa_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Gujrat_grbar.html')
def g79():
    return render_template('plots/Grouped_Bar_Charts/Gujrat_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Haryana_grbar.html')
def g80():
    return render_template('plots/Grouped_Bar_Charts/Haryana_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Himachal Pradesh_grbar.html')
def g81():
    return render_template('plots/Grouped_Bar_Charts/Himachal Pradesh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Jammu & Kashmir_grbar.html')
def g82():
    return render_template('plots/Grouped_Bar_Charts/Jammu & Kashmir_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Jharkhand_grbar.html')
def g83():
    return render_template('plots/Grouped_Bar_Charts/Jharkhand_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Karnataka_grbar.html')
def g84():
    return render_template('plots/Grouped_Bar_Charts/Karnataka_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Kerala_grbar.html')
def g85():
    return render_template('plots/Grouped_Bar_Charts/kerala_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Madhya Pradesh_grbar.html')
def g86():
    return render_template('plots/Grouped_Bar_Charts/Madhya Pradesh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Maharastra_grbar.html')
def g87():
    return render_template('plots/Grouped_Bar_Charts/Maharashtra_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Manipur_grbar.html')
def g88():
    return render_template('plots/Grouped_Bar_Charts/Manipur_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Meghalaya_grbar.html')
def g89():
    return render_template('plots/Grouped_Bar_Charts/Meghalaya_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Mizoram_grbar.html')
def g90():
    return render_template('plots/Grouped_Bar_Charts/Mizoram_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Nagaland_grbar.html')
def g91():
    return render_template('plots/Grouped_Bar_Charts/Nagaland_.html')
    
@app.route('/plots/Grouped_Bar_Charts/Odisha_grbar.html')
def g92():
    return render_template('plots/Grouped_Bar_Charts/Odisha_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Punjab_grbar.html')
def g93():
    return render_template('plots/Grouped_Bar_Charts/Punjab_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Sikkim_grbar.html')
def g94():
    return render_template('plots/Grouped_Bar_Charts/Sikkim_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Tamil Nadu_grbar.html')
def g95():
    return render_template('plots/Grouped_Bar_Charts/Tamil Nadu_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Telangana_grbar.html')
def g96():
    return render_template('plots//Telangana_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Tripura_grbar.html')
def g97():
    return render_template('plots/Grouped_Bar_Charts/Tripura_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Uttar Pradesh_grbar.html')
def g98():
    return render_template('plots/Grouped_Bar_Charts/Uttar Pradesh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Uttaranchal_grbar.html')
def g99():
    return render_template('plots/Grouped_Bar_Charts/Uttaranchal_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/West Bengal_grbar.html')
def g100():
    return render_template('plots/Grouped_Bar_Charts/West Bengal_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/A & N Islands_grbar.html')
def g101():
    return render_template('plots/Grouped_Bar_Charts/A & N Islands_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Chandigarh_grbar.html')
def g102():
    return render_template('plots/Grouped_Bar_Charts/Chandigarh_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/D & N Haveli and Daman & Diu_grbar.html')
def g103():
    return render_template('plots/Grouped_Bar_Charts/D & N Haveli and Daman & Diu_grbar.html')

 @app.route('/plots/Grouped_Bar_Charts/Delhi_grbar.html')
def g104():
    return render_template('plots/Grouped_Bar_Charts/Delhi_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Lakshadweep_grbar.html')
def g105():
    return render_template('plots/Grouped_Bar_Charts/Lakshadweep_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Puducherry_grbar.html')
def g106():
    return render_template('plots/Grouped_Bar_Charts/Pudducherry_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Rajasthan_grbar.html')
def g107():
    return render_template('plots/Grouped_Bar_Charts/Rajasthan_grbar.html')
    
@app.route('/plots/Grouped_Bar_Charts/Assam_grbar.html')
def g108():
    return render_template('plots/Grouped_Bar_Charts/Assam_grbar.html')
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
if __name__ == "__main__":
    app.run(debug=True)
