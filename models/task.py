# models/task.py

from sqlalchemy import Column, Integer, String
from database import Base

# SQLAlchemy model that represents the "tasks" table
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    status = Column(String(20), default="pending", nullable=False)
