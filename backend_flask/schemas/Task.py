from  pydantic import BaseModel
from typing import Optional

from ..models.Task import TaskStatus

class TaskBase(BaseModel):
  name: str
  status: Optional[TaskStatus] = TaskStatus.pending

class TaskCreate(TaskBase):
  list_id: int
  
class TaskRead(TaskBase):
  id:int
  list_id: int
  class Config :
    from_attributes=True