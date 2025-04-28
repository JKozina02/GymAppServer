from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def getHashedPassword(password: str):
    return pwd_context.hash(password)

def verifyPassword(hashedPassword: str, password: str):
    return pwd_context.verify(password, hashedPassword)

def createUser(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise ValueError("User with this email exists")

    hashed_password = getHashedPassword(user.password)
    db_user = models.User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def boolEmailExists(db: Session, user: schemas.LoginUser):
    return db.query(models.User).filter(models.User.email == user.email).first() is not None

def loginUser(db: Session, user: schemas.LoginUser):
    loggedIn = False
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not existing_user:
        raise ValueError("No account found with the provided email")
        
    if verifyPassword(existing_user.password, user.password):
        raise ValueError("Incorrect password")
    
    loggedIn = True
    return loggedIn

def getExercises(db: Session, name: str = None):
    if name:
        return db.query(models.Exercise).filter(models.Exercise.name.ilike(f"%{name}%")).all()
    else:
        return db.query(models.Exercise).all()
    
def createExercises(db: Session, exercise: schemas.ExerciseCreate):
    db_exercise = models.Exercise(name=exercise.name , time=exercise.time, reps=exercise.reps, weight=exercise.weight)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def deleteExercise(db: Session, exercise_id: int):
    exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if not exercise:
        raise ValueError("Exercise not found")
    db.delete(exercise)
    db.commit()
    return {"message": "Exercise deleted successfully"}

def updateExercise(db: Session, exercise_id: int, updated_data: schemas.ExerciseUpdate):
    exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if not exercise:
        raise ValueError("Exercise not found")
    exercise.name = updated_data.name if updated_data.name is not None else exercise.name
    exercise.time = updated_data.time if updated_data.time is not None else exercise.time
    exercise.reps = updated_data.reps if updated_data.reps is not None else exercise.reps
    exercise.weight = updated_data.weight if updated_data.weight is not None else exercise.weight
    
    db.commit()
    db.refresh(exercise)
    return exercise