from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class ExerciseCreate(BaseModel):
    name: str
    time: bool
    reps: bool
    weight: bool

class LoginUser(BaseModel):
    email: EmailStr
    password: str
    
class ExerciseUpdate(BaseModel):
    name: str | None = None
    time: bool | None = None
    reps: bool | None = None
    weight: bool | None = None