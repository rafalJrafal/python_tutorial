import json

var = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json_var = json.dumps(var, indent=4)

print(json_var)

converted_var = json.loads(json_var)

if "name" in converted_var:
    print("has a name")

for element in converted_var:
    print(element)

print(converted_var["cars"])

json.load()