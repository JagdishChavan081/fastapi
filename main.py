# -*- coding utf-8 -*-
#created on 8/11/2022
#@ code by: Jagdish Chavan

#pip install fastapi uvicorn

#import library
from statistics import variance
import uvicorn    #ASGI
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

#create the app object
app = FastAPI()
pickle_in=open('D:/fapi/code/classifier.pkl','rb')
classifier=pickle.load(pickle_in)

#Index routes, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Hello, World'}

#route with a single paramter, return the parameter within a message
#loacted at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name:str):
    return{'Welcome to code with jagutive':f'{name}'}

#Expose the prediction functionalit, make a prediction from the passed data
#JSON data and return the predicted bank Note
@app.post('/predict')
def predict_banknote(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    #print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction='Fake note'
    else:
        prediction='Its a Bank note'
    return {'prediction':prediction}



# Run the API with uvicorn
#will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)



#uvicorn main.app --reload


