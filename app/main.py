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
        crud.createUser(db, user)
        return {"status_code": 200, "message":"User created succesfully!"}
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        return HTTPException(status_code=500, detail=str(a))

@app.post("/check-user/")
def check_user(user: schemas.LoginUser, db: Session = Depends(get_db)):
    try:
        crud.boolEmailExists(db, user)
        return {"status_code": 200, "message":"Email valid!"}
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        return HTTPException(status_code=500, detail=str(a))

@app.post("/login-user/")
def login_user(user: schemas.LoginUser, db: Session = Depends(get_db)):
    try:
        crud.loginUser(db, user)
        return {"status_code": 200, "message":"User logged In!"}
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as a:
        return HTTPException(status_code=500, detail=str(a))