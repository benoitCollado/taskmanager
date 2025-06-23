from ...models import Task, TaskList, TaskStatus, Base
from ...schemas import TaskListRead

class TestTaskList:
  
  def test_empty_tasklist_list(self, client):
    response = client.get("/api/tasklist/")
    assert response.status_code == 200

  def test_two_tasklists(self, client, app):
    Base.metadata.drop_all(bind=app.config["DB_ENGINE"])
    Base.metadata.create_all(bind=app.config["DB_ENGINE"])
    
    list1 = TaskList(name="list test 1")
    list2 = TaskList(name="list test 2")
    db = app.config["SESSION_FACTORY"]()
    db.add_all([list1,list2])
    db.commit()

    _ = list1.tasks_list
    _ = list2.tasks_list

    response = client.get("/api/tasklist/")
    assert response.status_code == 200
    assert len(response.json) == 2

    validated = [TaskListRead.model_validate(task).model_dump() for task in response.json]
    assert validated[0]["id"] == list1.id
    assert validated[0]["name"] == list1.name
    assert validated[0]["tasks_list"] == list1.tasks_list
    assert validated[1]["id"] == list2.id
    assert validated[1]["name"] == list2.name
    assert validated[1]["tasks_list"] == list2.tasks_list
    db.close()
   

