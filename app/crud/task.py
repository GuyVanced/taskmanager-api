# crud operatios for tasks
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import task as taskModel
from ..schemas import task as taskSchema

def create(task : taskSchema.CreateTask, db: Session):
    new_task = taskModel.Task(title = task.title,
                              description = task.description,
                              completed = task.completed)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"Detail": "Task successfully Created"}

def get_all(db : Session):
    result = db.scalars(select(taskModel.Task)).all()

    return result

def get_by_id(id : int,db: Session):
    result = db.scalars(select(taskModel.Task).where(taskModel.Task.task_id == id)).first()
    
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    
    return result


def update_by_id(id : int, task : taskSchema.UpdateTask, db:Session):
    stmt = update(taskModel.Task).where(taskModel.Task.task_id == id).values(**task.model_dump(exclude_unset=True))

    result = db.execute(stmt)

    if result.rowcount==0:
        return HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Task with id : {id} not found")
    
    db.commit()

    return {"message" : f"Successfully updated task with id : {id}"}

def delete_by_id(id:int , db: Session):
    stmt = delete(taskModel.Task).where(taskModel.Task.task_id == id)

    result = db.execute(stmt)

    if result.rowcount==0:
        return HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Task with id : {id}not found")
    
    db.commit()

    return {"details": f"Successfully deleted task with id : {id}"}

