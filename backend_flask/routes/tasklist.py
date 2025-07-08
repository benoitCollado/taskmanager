from flask import Blueprint, jsonify, request
#from ..database import SessionLocal
from ..models.Task import Task, TaskStatus
from ..models.TaskList import TaskList
from ..schemas.Task import TaskRead, TaskCreate
from ..schemas.TaskList import TaskListRead, TaskListCreate
from ..utils.validationdecorator import validate_model
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from pydantic import ValidationError
from sqlalchemy import select, delete


def register_tasklist_routes(app, SessionLocal, prefix:str):
  tasklist_bp = Blueprint("tasklist",__name__)
  
  @tasklist_bp.route("/tasklist/", methods=["GET"])
  def get_tasklists():
    try:
      db = SessionLocal()
      results = db.query(TaskList).all()
      tasklists = [TaskListRead(id=result.id,name=result.name).model_dump() for result in results]
      db.close()
    except NoResultFound:
      return jsonify({"error": "No Tasklist Found"}), 404
    return jsonify(tasklists)
  
  @tasklist_bp.route("/tasklist/<int:tasklist_id>", methods=["GET"])
  def get_tasklist_details(tasklist_id):
    try :
      db = SessionLocal()
      tasklist = db.query(TaskList).filter(TaskList.id == tasklist_id).one() #mais possibilité d'utiliser one_or_none()
      tasklist = TaskListRead.model_validate(tasklist).model_dump()
      db.close()
    except NoResultFound:
      return jsonify({"error":"Tasklist Not Found"}),404
    except MultipleResultsFound:
      return jsonify({"error":"Multiple Tasklist Found"}), 400
    return tasklist

  @tasklist_bp.route("/tasklist/", methods=["POST"])
  @validate_model(TaskListCreate)
  def post_tasklist(validated_data):
    try:
      db = SessionLocal()
      tasklist = TaskList(name = validated_data.name)
      db.add(tasklist)
      db.commit()
      tasklist = TaskListRead.model_validate(tasklist).model_dump()
      db.close()
      print("on est là")
      return jsonify(tasklist), 201
    except ValidationError as exc :
      print(repr(exc.errors()[0]['type']))
      return jsonify({"error":"la validation des données n'est correcte"}), 400
    except Exception as e :
      e.add_note(f"{validated_data}")
      return jsonify({"error": f"une erreur est intervenue : {e}"}), 403
      
  @tasklist_bp.route("/tasklist/<int:list_id>", methods=["PUT", "PATCH"])
  @validate_model(TaskListCreate)
  def modify_taskList(validated_data, list_id):
    try:
      with SessionLocal() as session:
        sql = select(TaskList).where(TaskList.id == list_id)
        result = session.execute(sql).scalars().one()
        for key, value in validated_data.dict().items():
          setattr(result, key, value)
        session.commit()
        return jsonify({"message":f"la liste {list_id} a bien été modifiée"}), 201
    except ValidationError as exc :
      print(repr(exc.errors()[0]['type']))
      return jsonify({"error":"la validation des données n'est correcte"}), 400
    except Exception as e :
      e.add_note(f"{validated_data}")
      return jsonify({"error": f"une erreur est intervenue : {e}"}), 403  
    
  @tasklist_bp.route("/tasklist/<int:list_id>", methods=["DELETE"])
  def delete_taskList(list_id):
    try:
      with SessionLocal() as session:
        sql = delete(TaskList).where(TaskList.id == list_id)
        session.execute(sql)
        session.commit()
        return jsonify({"message":f"la liste {list_id} a bien été supprimée"}), 204
    except ValidationError as exc :
      print(repr(exc.errors()[0]['type']))
      return jsonify({"error":"la validation des données n'est correcte"}), 400
    except Exception as e :
      print("une erreur est survenue", e)
      return jsonify({"error": f"une erreur est intervenue : {e}"}), 403  

  app.register_blueprint(tasklist_bp, url_prefix=prefix)