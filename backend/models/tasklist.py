from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from ..database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from task import Task

class TaskList(Base):
  __tablename__ = "task_lists"

  id: Mapped[int] = mapped_column(index=True, primary_key=True)
  name: Mapped[str] = mapped_column(nullable=False)
  tasks: Mapped[list["Task"]] = relationship(back_populates="list", cascade="all, delete")