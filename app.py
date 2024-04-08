from flask import Flask, render_template,request
import joblib
name='xyz@gmail.com'
pas='python'

model = joblib.load('Log.pkl')
app=Flask(__name__)

@app.route('/')
def home():
    a=request.form.get('email adress')
    print(a)
    return render_template('home.html')

@app.route('/events')
def events():
    return render_template('events.html')


# names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']-->
@app.route('/submit',methods=['post'])
def submit():

    a=eval(request.form.get('Pregnancies'))
    b = eval(request.form.get('Glucose'))
    c = eval(request.form.get('BloodPressure'))
    d = eval(request.form.get('SkinThickness'))
    e = eval(request.form.get('Insulin'))
    f = eval(request.form.get('BMI'))
    g = eval(request.form.get('DiabetesPedigreeFunction'))
    h = eval(request.form.get('Age'))
    res1=model.predict([[a,b,c,d,e,f,g,h]])
    if res1[0]==1:
        return "Diabetic"
    else:
        return "Not Diabetic"


@app.route('/contact')
def contact():
    return render_template('contact.html')



app.run(debug=True)#required to let the app run on ec2
#app.run(host="0.0.0.0",debug=True)#required to let the app run on ec2
#Get is something retreive from backend
# @app.route('/submit',methods = ['post'])
# def submit():
#     a = request.form.get('Email_Address')
#     b = request.form.get('mobile_number')
#     c = request.form.get('password')
#     print(a,b,c)
#     if (a==name) and (c==pas):
#         return ("Log in")
#     else:
#         return ('incrct')