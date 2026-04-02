from pydantic import BaseModel

class State(BaseModel):
    problem: str
    difficulty: str

class Action(BaseModel):
    code: str

class StepResult(BaseModel):
    reward: float
    done: bool
    info: dict