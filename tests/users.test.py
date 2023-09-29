import requests
import uuid
import bcrypt

BaseUrl = "http://localhost:5000/api/users"

test1 = requests.get(f"{BaseUrl}/f05f7862-601a-4e54-8799-a01b7e3a8d2a")
print(test1.json())

test2 = requests.get(f"{BaseUrl}")
print(test2.json())

password = 'foobar'
bytes = password.encode('utf-8')
NewUser = {"id": str(uuid.uuid4()),
           "name": "Amy Fowler",
           "email": "amyfowler@gmail.com",
           "password": bcrypt.hashpw(bytes, bcrypt.gensalt()).decode('utf-8')
          }
headers = {'Content-Type': 'application/json'}
test3 = requests.post(f"{BaseUrl}", json=NewUser, headers=headers)
print(test3.json())
