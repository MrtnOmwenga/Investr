from flask import Blueprint, abort, jsonify, make_response, request

from models.engine import session
from models.users import Users

users = Blueprint('users', __name__)

@users.route("/", methods=['GET'], strict_slashes=False)
def GetUsers():
  results = session.query(Users)
  data = []
  for user in results:
     data.append(user.to_dict())
  
  response = jsonify(data)
  response.status_code = 200

  return response

@users.route("/<id>", methods=['GET'], strict_slashes=False)
def GetUserById(id):
  result = session.query(Users).filter(Users.id == id).one()

  response = jsonify(result.to_dict())
  response.status_code = 200
  return response

@users.route("/<email>", methods=['GET'], strict_slashes=False)
def GetUserByEmail(email):
  result = session.query(Users).filter(Users.email == email).one()

  response = jsonify(result.to_dict())
  response.status_code = 200
  return response

@users.route("/", methods=['POST'], strict_slashes=False)
def PostUser():
  if not request.get_json():
    abort(400, description="Not a JSON")

  print(request.get_json())
  if 'name' not in request.get_json():
     abort(400, description="Missing name")
  if 'email' not in request.get_json():
      abort(400, description="Missing email")
  if 'password' not in request.get_json():
      abort(400, description="Missing password")

  data = request.get_json()
  print(data)
  instance = Users(**data)
  session.add(instance)
  session.commit()
  return make_response(jsonify(instance.to_dict()), 201)
