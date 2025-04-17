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

    # if validateEmail(emailToValidate):
    #     hashPassword = getHashedPassword(password)
    #     users.append(User(
    #         username=username,
    #         email=emailToValidate,
    #         password=hashPassword
    #     ))
    #     return "Email valid"
    # else:
    #     return "Email already exists"

# def loginUser(email: EmailStr, password: str):
#     return (user.email == email and verifyPassword(user.password, password) for user in users)

