from pydantic import BaseModel, EmailStr, ValidationError
from typing import List
from passlib.context import CryptContext

# Users-----------------------------------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def getHashedPassword(password: str):
    return pwd_context.hash(password)

# Returns true if password is correct
def verifyPassword(hashedPassword: str, password: str):
    return pwd_context.verify(password, hashedPassword)

# Create new user, validate email, hash password
def createUser(username: str, email: str, password: str):
    try:
        emailToValidate: EmailStr = email
    except ValidationError:
        return "Invalid email format"
    
    if validateEmail(emailToValidate):
        hashPassword = getHashedPassword(password)
        users.append(User(
            username=username,
            email=emailToValidate,
            password=hashPassword
        ))
        return "Email valid"
    else:
        return "Email already exists"

def loginUser(email: EmailStr, password: str):
    return any(user.email == email and verifyPassword(user.password, password) for user in users)

# We don't want emails to repeat, any returns true if there is email in the list, so we use not
def validateEmail(email: EmailStr):
    return not any(user.email == email for user in users)

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

users: List[User] = []



#Exercises-------------------------------------------------------------------------------------
class Exercise(BaseModel):
    id: int
    name: str
    time: bool
    reps: bool
    weight: bool

exercises: List[Exercise] = [
    Exercise(
        id=0,
        name="Bench Press",
        time=False,
        reps=True,
        weight=True
    ),
    Exercise(
        id=1,
        name="Clean and Jerk",
        time=False,
        reps=True,
        weight=True
    ),
]