from ...models import Task, TaskList, TaskStatus
from ...schemas import TaskListRead



class TestTaskList:

  def test_tasklist_list(self, client):
    payload={"name":"un nom de liste"}
    response = client.post("/api/tasklist/", json=payload)
    assert response.status_code == 201
    validated = TaskListRead.model_validate(response.get_json()).model_dump()
    assert validated["name"] == payload["name"]
