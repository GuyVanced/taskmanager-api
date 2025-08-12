# route handling
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from fastapi import APIRouter, status,Depends
from ..core import database
from ..crud import task as task_crud
from ..schemas import task as task_schema

router = APIRouter(prefix="/tasks", tags= ["TASK_API"])

get_db = database.get_db

@router.get("/", response_model = List[task_schema.TaskResponse],  status_code= status.HTTP_200_OK)
def view_tasks(db : Session = Depends(get_db)):
    return task_crud.get_all(db)

@router.get("/{id}", response_model=task_schema.TaskBase, status_code=status.HTTP_200_OK)
def view_task(id: int, db:Session = Depends(get_db)):
    return task_crud.get_by_id(id , db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task : task_schema.CreateTask, db : Session = Depends(get_db)):
    return task_crud.create(task, db)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_task(task: task_schema.UpdateTask, id : int, db : Session = Depends(get_db)):
    return task_crud.update_by_id(id, task, db)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_task(id : int, db : Session=Depends(get_db)):
    return task_crud.delete_by_id(id, db)






