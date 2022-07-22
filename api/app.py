import pymongo as mongo 
import numpy as np 

from fastapi import FastAPI
from csv import DictReader

from functools import lru_cache

with open("./jojo-stand-stats.csv", newline='', encoding='utf-8') as file:
    
    data : list[dict] = [ stand for stand in DictReader(file) ] 

    data : np.ndarray = np.array(data)


app = FastAPI()


@lru_cache(2000)
@app.get("/api/v2")
async def default():
    return {"_message": "Hello, You are connected with JoJo API"}


@lru_cache(2000)
@app.get("/api/v2/stands")
async def get_all_stands(): 
    return list(data) 

@lru_cache(2000)
@app.get("/api/v2/stands/{stand_id}")
async def get_stand(stand_id: int):

    if stand_id >= len(data):
        return {"_message": "stand out of bounds"}

    return data[stand_id]






"""
TODO:
    έχεις δύο επιλογές.

    Α. κάνεις από εδώ insert το `data` στην mongodb 

    Β. Κάνεις write το `data` ως json αρχείο και μετά πας στο dockercompose και το βάζεις εκεί manually 
       Έτσι γλυτώνεις api calls αλλά θα είναι ένα μοναδιαίο αρχείο hardcoded

"""


# How to run program
# uvicorn app:app --reload  (--reload for debugging)
