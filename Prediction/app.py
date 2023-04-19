import pickle
import pandas as pd
import numpy as np

rap = pickle.load(open('F:\Final Year Project\Prediction\kmean.pkl','rb'))

features = [32,	5150,	12361,	14835,	420	,38918,	28,	402601,	1737,	2023	]
final_features = [np.array(features)] 
y_pred = rap.predict(final_features)
if y_pred[0] == 1:         
    label="Very low rate crime area"
elif y_pred[0] == 3:
    label="Low rate crime area"
elif y_pred[0] == 2:
    label="High rate crime area"
elif y_pred[0] == 4:
    label="very high rate crime area"
print(label)