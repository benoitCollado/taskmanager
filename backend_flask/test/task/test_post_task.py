from operator import add
from ...models import Base, Task, TaskList, TaskStatus
from ...schemas import TaskCreate, TaskRead, TaskListRead
from sqlalchemy import select

class TestPostTask:
  def test_post__task(self,client, app):
    Base.metadata.drop_all(bind=app.config["DB_ENGINE"])
    Base.metadata.create_all(bind=app.config["DB_ENGINE"])
    db = app.config["SESSION_FACTORY"]
    tasklit = TaskList(name="tasklist test")
    db.add(tasklit)
    db.commit()
    
    payload = {"name":"test du post sur task", "status" : TaskStatus.in_progress, "list_id" : 1}
    response = client.post("/api/task/", json=payload)
    assert response.status_code == 201
    assert TaskRead.model_validate(response.get_json())
    