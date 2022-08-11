# -*- coding utf-8 -*-
#created on 8/11/2022
#@ code by: Jagdish Chavan

#pip install fastapi uvicorn

#import library
import uvicorn    #ASGI
from fastapi import FastAPI

#create the app object
app = FastAPI()

#Index routes, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Hello, World'}

#route with a single paramter, return the parameter within a message
#loacted at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name:str):
    return{'Welcome to code with jagutive':f'{name}'}


# Run the API with uvicorn
#will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)



#uvicorn main.app --reload


