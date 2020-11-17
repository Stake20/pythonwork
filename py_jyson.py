
import json
# Sample Json
userJSON = '{"first_name": "John", "lastname": "Doe", "age": 30}'
# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year':1970}

carJson = json.dumps(car)

print(carJson)