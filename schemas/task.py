# schemas/task.py

from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title="Título da Tarefa",
        description="Digite um título curto e claro para a tarefa",
        example="Estudar FastAPI"
    )
    description: Optional[str] = Field(
        None,
        max_length=300,
        title="Descrição",
        description="Descrição opcional com até 300 caracteres",
        example="Revisar o uso de routers e schemas no projeto"
    )
    completed: bool = Field(
        False,
        title="Concluída?",
        description="Status da tarefa (True = feita, False = pendente)",
        example=False
    )

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int    

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)
