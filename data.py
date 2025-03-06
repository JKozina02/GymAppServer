from pydantic import BaseModel
from typing import List

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
        weight=True),

    Exercise(
        id=1,
        name="Clean and Jerk", 
        time=False, 
        reps=True, 
        weight=True),
]