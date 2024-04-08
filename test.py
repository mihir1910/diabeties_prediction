import joblib

pred=joblib.load('Log.pkl')
res=pred.predict([[5,105,72,29,325,36.9,0.159,28],[1,2,3,4,5,5,7,8],[100,100,100,100,100,1001,100,100]])
print(res)