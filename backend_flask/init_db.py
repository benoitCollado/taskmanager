from .database import SessionLocal, engine, Base
from .models import Task, TaskStatus, TaskList

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

list1 = TaskList(name="Liste de Test")
task1 = Task(name="Acheter du pain", status=TaskStatus.pending, list=list1)
task2 = Task(name="Finir le projet", status=TaskStatus.pending, list=list1)

db.add(list1)
db.add_all([task1, task2])
db.commit()

list2 = TaskList(name="Liste de Test 2")
task3 = Task(name="Acheter du pain 2", status=TaskStatus.pending, list=list2)
task4 = Task(name="Finir le projet 2", status=TaskStatus.pending, list=list2)

db.add(list2)
db.add_all([task3, task4])
db.commit()

db.close()

print("données initialisées avec succès")
