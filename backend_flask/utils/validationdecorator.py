from functools import wraps
from flask import request, jsonify, wrappers
from pydantic import BaseModel, ValidationError
from typing import Type

def validate_model(model_class : Type[BaseModel]):
  def decorator(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
      try :
        data = request.get_json()
        validated_data = model_class.model_validate(data)
        return f(validated_data, *args, **kwargs)
      except ValidationError as e:
        return jsonify({"error":e.errors()}),400

    return wrapper
  return decorator