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

db.close()

print("données initialisées avec succès")
