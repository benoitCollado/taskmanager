from typing import List, Optional
from pydantic import BaseModel

from .task import TaskRead

class TaskListBase(BaseModel):
  name:str

class TaskListCreate(TaskListBase):
  pass

class TaskListRead(TaskListBase):
  id:int
  tasks : List[TaskRead] = [] #pour apparaitre il faut que le champs ait le même nom dans le modèle et les schéma de validation.
  class Config :
    from_attributes = True

class TaskListUpdate(BaseModel):
  name: Optional[str]=None
  