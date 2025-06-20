from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from ..database import Base
from typing import TYPE_CHECKING
import enum

if TYPE_CHECKING:
  from TaskList import TaskList

class TaskStatus(str, enum.Enum):
  pending = "pending"
  in_progress = "in_progress"
  done = "done"

class Task(Base):
  __tablename__ = "task"
  
  id:Mapped[int] = mapped_column(index=True, primary_key=True)
  name:Mapped[str] = mapped_column(nullable=False)
  status:Mapped[TaskStatus] = mapped_column(Enum(TaskStatus),default=TaskStatus.pending)
  list_id:Mapped[int] = mapped_column(ForeignKey("task_list.id"))

  list: Mapped["TaskList"] = relationship(back_populates="tasks_list")
  