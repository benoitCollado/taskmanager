from fastapi import APIRouter, Depends, HTTPException
#from sqlalchemy.engine import result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import Annotated

from ..database import get_db
from ..models.task import Task
from ..models.tasklist import TaskList
from ..schemas.task import TaskCreate, TaskRead
from ..schemas.task_list import TaskListCreate, TaskListRead, TaskListUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/lists/", response_model = TaskListRead)
async def create_task_list(task_list: TaskListCreate, db: AsyncSession = Depends(get_db)):
  new_list = TaskList(name=task_list.name)
  db.add(new_list)
  await db.commit()
  await db.refresh(new_list)
  return new_list

@router.get('/lists/', response_model=list[TaskListRead])
async def read_task_lists(db: Annotated[AsyncSession, Depends(get_db)]):
  # le select in load est necessaire pour avoir la liste des tasks associées à la tasklist sinon elle restera vide 
  result = await db.execute(select(TaskList).options(selectinload(TaskList.tasks)))
  return result.scalars().all()

@router.get('/lists/{task_list_id}', response_model=list[TaskListRead])
async def read_task_list(task_list_id: int, db: AsyncSession = Depends(get_db)):
  task_list = select(TaskList).where(TaskList.id == task_list_id)
  result = await db.execute(task_list)
  return result.scalars().all()

@router.put('/lists/{task_list_id}', response_model=TaskListRead)
async def update_task_list(task_list_id:int,update_list:TaskListUpdate, db: Annotated[AsyncSession, Depends(get_db)]):
  result = await db.execute(select(TaskList).where(TaskList.id == task_list_id))
  task_list = result.scalar_one_or_none()

  if task_list is None:
    raise HTTPException(detail="la liste n'a pas été trouvée", status_code=404)

  if update_list.name is not None:
    task_list.name = update_list.name

  await db.commit()
  await db.refresh(task_list)
  return task_list

@router.delete("/lists/{task_list_id}", status_code=204)
async def delete_task_list(task_list_id:int, db: Annotated[AsyncSession ,Depends(get_db)]):
  result = await db.execute(select(TaskList).where(TaskList.id == task_list_id))
  task_list = result.scalar_one_or_none()

  if task_list is None:
    raise HTTPException(status_code=204, detail="task list introuvable")

  await db.delete(task_list)
  await db.commit()
  return None

@router.get("/", response_model=list[TaskRead])
async def get_tasks(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(Task).where(Task.status == "pending"))
    return result.scalars().all()