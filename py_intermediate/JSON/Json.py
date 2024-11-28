#  JSON -Javascript object notation - lightweight dataformat - data exchange, for web application
import json
from email.policy import default

from aiohttp.typedefs import JSONEncoder
from faraday_agent_dispatcher.config import instance

#  serialisation or encoding, - converting dictionary to JSON

person = {"name": "John", "age": 25, "city": "New york", "has_kids": False, "titles": ["Security Engineer", "Designer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)   # sort_keys- sort alphabetically, indent-line break,
print(personJSON)


with open("person.json", "w") as file:
    json.dump(person, file, indent=4)


# Deserialization - turning Json data back to dictionary

# person = json.loads(personJSON)
# print(person)

#  method 2

with open("person.json", "r") as file:
    person = json.loads(personJSON)
    print(person)

#  custom encoder for custom object - json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 20)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError ("Object of type User is not JSON serializable")

# userJSON = json.dumps(user, default=encode_user)

# Method 2 -  encoding JSON Object
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# userJSON = json.dumps(user, cls=UserEncoder)

userJSON = UserEncoder().encode(user)
print(userJSON)

# Decoding custom objects to normal python objects

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(user.name)



