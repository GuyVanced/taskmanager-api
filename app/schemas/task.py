# pydantic schemas
from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title : str
    description : str
    completed : bool

class CreateTask(TaskBase):
    pass

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description : Optional[str] = None
    completed : Optional[bool] = None

class TaskResponse(TaskBase):
    id : int

    class Config():
        orm_mode = True






