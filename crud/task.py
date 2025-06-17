# crud/task.py

from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(title=task_data.title, is_done=task_data.is_done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
