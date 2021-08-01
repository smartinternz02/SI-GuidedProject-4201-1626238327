from flask import Flask,render_template,request
import pickle
import pickle,joblib
model=pickle.load(open('wri.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/login',methods=["POST"])
def func2():
    car_ID=request.form['car_ID']
    wheelbase=request.form['wheelbase']
    carlength=request.form['carlength']
    carwidth=request.form['carwidth']
    carheight=request.form['carheight']
    curbweight=request.form['curbweight']
    enginesize =request.form['enginesize']
    boreratio=request.form['boreratio']
    stroke=request.form['stroke']
    compressionratio=request.form['compressionratio']
    horsepower=request.form['horsepower']
    peakrpm=request.form['peakrpm']
    citympg=request.form['citympg']
    data=[[int(car_ID),float(wheelbase),float(carlength),float(carwidth),float(carheight),int(curbweight),int(enginesize),float(boreratio),float(stroke),float(compressionratio),int(horsepower),int(peakrpm),int(citympg)]]
    pred=model.predict(data)
    print(pred[0])
    return render_template("index.html",y= 'CAR MPG is '+str(pred))
if __name__=='__main__':
   app.run(debug= True)
