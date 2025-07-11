from typing import Optional
from pydantic import BaseModel

from ..models.task import TaskStatus

class TaskBase(BaseModel):
  name:str
  status: Optional[TaskStatus] = TaskStatus.pending

class TaskCreate(TaskBase):
  list_id:int

class TaskRead(TaskBase):
  id:int
  list_id:int
  class Config:
    from_attributes = True



