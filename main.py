from fastapi import FastAPI, HTTPException
from typing import List

import data as dt

app = FastAPI()

Items: List[dt.Exercise] = dt.exercises

@app.get("/")
def read_root():
    return {"Item" : Items[0]}

@app.get("/exercise/{exercise_id}", response_model=dt.Exercise)
def read_exercise(exercise_id: int):
    try:
        return Items[exercise_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Exercise not found")