import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
df=pd.read_csv(url,names=names)

X=df.iloc[:, :-1]
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

res=model.score(X_test,y_test)
print(res)

r=model.predict([[9,156,86,28,155,34.3,1.189,42],[1,2,3,4,5,6,7,8]])
print(r)
joblib.dump(model,"Log.pkl")