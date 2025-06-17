#!/usr/bin/python

import asyncio
from database import engine, async_session_local, Base
from models import TaskList, Task

print(f"Nom du module = {__name__}")

async def init_db():
  async with engine.begin() as conn :
    await conn.run_sync(lambda sync_conn: Base.metadata.drop_all(bind=sync_conn))
    await conn.run_sync(lambda sync_conn: Base.metadata.create_all(bind=sync_conn))

  async with async_session_local() as session :
    new_list = TaskList(name="première liste")
    session.add(new_list)
    await session.flush()

    task1 = Task(name="faire A", list_id = new_list.id)
    task2 = Task(name="faire B", list_id = new_list.id)

    session.add_all([task1, task2])
    
    new_list2 = TaskList(name="deuxieme liste")
    session.add(new_list2)
    await session.flush()

    task3 = Task(name="faire C", list_id = new_list2.id)
    task4 = Task(name="faire D", list_id = new_list2.id)

    session.add_all([task3, task4])
    await session.commit()

    print("base initialisée avec des données")

if __name__ == "__main__":
    print("ici")
    asyncio.run(init_db())

