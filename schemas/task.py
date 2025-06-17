from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# Enum de status da tarefa
class TaskStatus(str, Enum):
    pending = "pending"
    done = "done"

# Base model com campos compartilhados
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
    status: TaskStatus = Field(
        TaskStatus.pending,
        title="Status",
        description="Status da tarefa (pending ou done)",
        example="pending"
    )

# Modelo para criação (usa tudo do base)
class TaskCreate(TaskBase):
    pass

# Modelo para atualização (campos opcionais)
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    status: Optional[TaskStatus] = None

# Modelo de retorno com ID
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
