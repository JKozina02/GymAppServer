from fastapi import FastAPI, HTTPException
from typing import List

import data as dt

app = FastAPI()

Items: List[dt.Exercise] = dt.exercises
Users: List[dt.User] = dt.users

#User login and veryfication

#Create new user
@app.post("/create-user/")
def create_user(email: str, username: str, password: str):
    try:
        dt.createUser(username=username, email=email, password=password)
        return {"status-code" : 201, "description": 'User created succesfully'}
    except ValueError as a:
        raise HTTPException(status_code=401, detail=a)
    
@app.post("/login-user/")
def login_user(email: str, password: str):
    if dt.loginUser(email, password):
        return {"status-code" : 202, "description": 'Logged in'}
    else:
        raise HTTPException(status_code=402, detail="Wrong email or password")
    
#Exercise 
@app.get("/exercise/{exercise_id}", response_model=dt.Exercise)
def read_exercise(exercise_id: int):
    try:
        return Items[exercise_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
