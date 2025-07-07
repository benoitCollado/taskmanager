from flask import Blueprint, jsonify
from pydantic import ValidationError
#from ..database import SessionLocal
from ..models.Task import Task, TaskStatus
from ..schemas.Task import TaskRead, TaskCreate
from ..schemas.TaskList import TaskListRead, TaskListCreate
from ..utils.validationdecorator import validate_model
from typing import Type
from sqlalchemy import select, delete



def register_task_routes(app, SessionLocal, prefix:str):

  task_bp = Blueprint("tasks", __name__)
  
  @task_bp.route("/task/", methods=["GET"])
  def get_tasks():
    try:
      db = SessionLocal()
      tasks = db.query(Task).filter(Task.status == TaskStatus.pending).all()
      result = [TaskRead.model_validate(t).model_dump() for t in tasks]
      db.close()
      return jsonify(result),200
    except ValidationError as e:
      print(f"500-erreur de validation des données : {e}")
      return jsonify({"error": "data validation error"}),500
    except Exception as e:
      print(f"500-une erreur est intervenue : {e}")
      return jsonify({"error": "an error occured"}), 500

  @task_bp.route("/task/<int:task_id>",methods=["GET"])
  def get_task_with_id(task_id):
    try :
      db = SessionLocal()
      task = db.query(Task).filter(Task.id == task_id).one()
      validated = TaskRead.model_validate(task).model_dump()
      db.close()
      return jsonify(validated), 200
    except ValidationError as e:
      print(f"500-erreur de validation des données : {e}")
      return jsonify({"error": "data validation error"}),500
    except Exception as e:
      print(f"500-une erreur est intervenue : {e}")
      return jsonify({"error": "unknow error"}), 500

  @task_bp.route("/task/",methods=["POST"])
  @validate_model(TaskCreate)
  def post_task(validated_data):
    try: 
      db = SessionLocal()
      if validated_data.status:
        task = Task(name = validated_data.name, status=validated_data.status, list_id= validated_data.list_id)
      else :
        task = Task(name = validated_data.name, list_id= validated_data.list_id)
      db.add(task)
      db.commit()
      validated = TaskRead.model_validate(task).model_dump()
      return jsonify(validated), 201
    except ValidationError as e:
      print(f"500-erreur de validation des données : {e}")
      return jsonify({"error":"data balidation error"}),500
    except Exception as e:
      print(f"500-Une erreur est intervenue : {e}")
      return jsonify({"error":"an error occured"}),500
    
  @task_bp.route("/task/<int:task_id>", methods=["DELETE"])
  def delete_task(task_id):
    try:
      db = SessionLocal()
      sql = delete(Task).where(Task.id == task_id)
      db.execute(sql)
      db.commit()
      db.close()
      return jsonify({"message":f"la tache {task_id} est bie supprimée"}),204
    except Exception as e:
      print("erreur dans le suppression de la tâche")
      return jsonify({"error":"an error occured"}),500

    
      

  app.register_blueprint(task_bp, url_prefix = prefix)

