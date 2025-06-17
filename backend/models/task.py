from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from database import Base
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tasklist import TaskList

class TaskStatus(str, enum.Enum):
  pending = "pending"
  in_progress = "in_progress"
  done = "done"

class Task(Base):

  __tablename__ = "tasks"
  
  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  name: Mapped[str] = mapped_column(nullable=False)
  status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus),default = TaskStatus.pending)
  list_id: Mapped[int] = mapped_column(ForeignKey("task_lists.id"))

  list: Mapped["TaskList"] = relationship(back_populates="tasks")



