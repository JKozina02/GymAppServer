from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database
from app.database import get_db, init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

@app.post("/create-user/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user = crud.createUser(db, user)
        return {"status_code":200, "message":"User created succesfully!", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))

@app.get("/check-user/")
def check_user(user: schemas.LoginUser, db: Session = Depends(get_db)):
    try:
        ans = crud.boolEmailExists(db, user)
        return {"status_code":200, "message":"Email valid!", "userExists":ans}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))

@app.post("/login-user/")
def login_user(user: schemas.LoginUser, db: Session = Depends(get_db)):
    try:
        loggedIn = crud.loginUser(db, user)
        return {"status_code":200, "message":"User logged In!", "loggedIn": loggedIn}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))
    
@app.get("/get-exercises/")
def get_exercises(name: str = None, db: Session = Depends(get_db)):
    try:
        exercises = crud.getExercises(db, name)
        return {"status_code":200, "exercises":exercises}
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))
    
@app.post("/create-exercise/")
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    try:
        exercise = crud.createExercises(db, exercise)
        return {"status_code":200, "message":"Exercise created succesfully!", "exercise": exercise}
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))
    
@app.delete("/delete-exercise/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    try:
        result = crud.deleteExercise(db, exercise_id)
        return {"status_code": 200, "message": result["message"]}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))
    
@app.put("/update-exercise/{exercise_id}")
def update_exercise(exercise_id: int, updated_data: schemas.ExerciseUpdate, db: Session = Depends(get_db)):
    try:
        updated_exercise = crud.updateExercise(db, exercise_id, updated_data)
        return {"status_code": 200, "message": "Exercise updated successfully", "exercise": updated_exercise}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))