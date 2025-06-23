from flask import Blueprint, jsonify
from ..database import SessionLocal
from ..models.Task import Task, TaskStatus
from ..schemas.Task import TaskRead, TaskCreate
from ..schemas.TaskList import TaskListRead, TaskListCreate
from ..utils.validationdecorator import validate_model
from sqlalchemy import select

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks/", methods=["GET"])
def get_tasks():
  db = SessionLocal()
  tasks = db.query(Task).where(Task.status == TaskStatus.pending).all()
  result = [TaskRead.model_validate(t).model_dump() for t in tasks]
  db.close()
  return jsonify(result)

