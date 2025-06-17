# models/task.py

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# SQLAlchemy model that represents the "tasks" table
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
