from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .Base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from Task import Task

class TaskList(Base):
  __tablename__ = "task_list"
  
  id:Mapped[int] = mapped_column(index=True, primary_key=True)
  name:Mapped[str] = mapped_column(nullable=False)
  tasks_list: Mapped[list["Task"]] = relationship(back_populates="list", cascade="all, delete")