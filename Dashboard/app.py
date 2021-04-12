from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app= Flask(__name__)

#predict

@app.route('/', methods= ['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/dataset', methods= ['POST','GET'])
def dataset():
    return render_template('dataset.html')

@app.route('/data_visualization', methods= ['POST','GET'])
def data_visualization():
    return render_template('data_visualization.html')

@app.route('/predict', methods= ['POST','GET'])
def predict():
    return render_template('predict.html')

#result
@app.route('/result', methods= ['POST','GET'])
def result():
    if request.method == 'POST':
        input= request.form

        df_predict= pd.DataFrame({
            'pdays': [input['pdays']], #input sesuai name yang ada di predict
            'previous': [input['previous']],
            'emp.var.rate': [input['emp.var.rate']],
            'cons.price.idx': [input['cons.price.idx']],
            'cons.conf.idx': [input['cons.conf.idx']],
            'euribor3m': [input['euribor3m']],
            'nr.employed': [input['nr.employed']],
        })

        prediksi= model.predict_proba(df_predict)[0][1]

        if prediksi>0.5:
            pred= 'Yes'
        else:
            pred= 'No'

        return render_template('result.html', data= input, pred= pred, prob= round(prediksi,2))
    
@app.route('/datavisual-details', methods= ['POST','GET'])
def datavisualdetails():
    return render_template('datavisual-details.html')

@app.route('/about', methods= ['POST','GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    filename= 'Final Project.sav'
    model= pickle.load(open(filename, 'rb'))
    app.run(debug=True)

