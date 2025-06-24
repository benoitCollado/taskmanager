from ...models import Task,TaskList, Base
from ...schemas import TaskRead,TaskListRead
from sqlalchemy import select

class TestGetTask:
  def test_get_one_task(self, client, app):
    Base.metadata.drop_all(bind=app.config["DB_ENGINE"])
    Base.metadata.create_all(bind=app.config["DB_ENGINE"])
    
    db = app.config["SESSION_FACTORY"]
    list1 = TaskList(name="liste 1 de test")
    db.add(list1)
    db.commit()
    list_validated = TaskListRead.model_validate(db.query(TaskList).filter(TaskList.id == 1).one()).model_dump()
    task1 = Task(name="tâche de test", list_id=list_validated["id"])
    db.add(task1)
    db.commit()

    response = client.get("/api/task/")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
    validated_data = [TaskRead.model_validate(task).model_dump() for task in response.get_json()]
    assert validated_data[0]["name"] == task1.name
    assert validated_data[0]["list_id"] == task1.list_id
    assert validated_data[0]["status"] == task1.status
    assert validated_data[0]["id"] == task1.id

  def test_get_two_tasks(self, client, app):
    Base.metadata.drop_all(bind=app.config["DB_ENGINE"])
    Base.metadata.create_all(bind=app.config["DB_ENGINE"])

    db = app.config["SESSION_FACTORY"]
    list1 = TaskList(name="liste 1 de test")
    db.add(list1)
    db.commit()
    list_validated = TaskListRead.model_validate(db.execute(select(TaskList).where(TaskList.id == 1)).scalar_one()).model_dump()
    task1 = Task(name="tâche de test", list_id=list_validated["id"])
    task2 = Task(name="tâche de test2", list_id=list_validated["id"])
    list_task = [task1,task2]
    db.add_all(list_task)
    db.commit()

    response = client.get("/api/task/")
    assert response.status_code == 200
    assert len(response.get_json()) == 2
    validated_data  = [TaskRead.model_validate(task).model_dump() for task in response.get_json()]
    valideted_data = sorted(validated_data, key = lambda x : x["id"] )
    list_task = sorted(list_task, key=lambda x: x.id)
    for inserted, get in zip(list_task, validated_data):
      assert inserted.id == get["id"]
      assert inserted.name == get["name"]
      assert inserted.status == get["status"]
      assert inserted.list_id == get["list_id"]    