from pydantic import BaseModel
from typing import Optional, List

from Task import TaskRead

class TaskListBase(BaseModel):
  name:str

class TaskListCreate(TaskListBase):
  pass

class TaskListRead(TaskListBase):
  id:int
  tasks_list: List[TaskRead]
  class config:
    from_attributes = True