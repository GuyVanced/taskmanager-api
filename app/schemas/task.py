# pydantic schemas
from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title : str = Field(...,min_length=3, description="Title must be atleast 3 characters")
    description : str
    completed : bool

class CreateTask(TaskBase):
    pass

# To allow users to optionally update choosen fields
class UpdateTask(BaseModel):
    title : str = Field(None,min_length=3, description="Title must be atleast 3 characters")
    description : Optional[str] = None
    completed : Optional[bool] = None

# To return all Task details including the id
class TaskResponse(TaskBase):
    task_id : int

    class Config():
        orm_mode = True






