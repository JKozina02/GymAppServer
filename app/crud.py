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
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not existing_user:
        raise ValueError("No account found with the provided email")
    
    if not verifyPassword(existing_user.password, user.password):
        raise ValueError("Incorrect password")
    
    return existing_user
