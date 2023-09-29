import uuid
import bcrypt
from models.engine import session
from models.users import Users

def Login(email, password):
  result = session.query(Users).filter(Users.email == email).one()

  if bcrypt.checkpw(password.encode('utf-8'), result.password.encode('utf-8')):
    return result
  else:
    return None

def Register(name, email, password):
  bytes = password.encode('utf-8')
  NewUser = Users(
    id= str(uuid.uuid4()),
    name = name,
    email = email,
    password = bcrypt.hashpw(bytes, bcrypt.gensalt()).decode('utf-8')
  )

  try:
    session.add(NewUser)
    session.commit()

    return NewUser
  except Exception:
    return None
