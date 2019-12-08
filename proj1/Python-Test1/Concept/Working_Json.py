'''
Just a quick reference on how to work with json data

Module
    import json

Methods
    dump    -- dump json to file
    dumps   -- dump json to object/variable
    load    -- load json from file
    loads   -- load json from object/variable

Notes:
    object_hook: This is an option parameter when used returns a custom object instead of dict.
                 This is typically used with load, loads. See morsels_easyjson for more information

'''


import requests
import json
print('#'*50)
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
print("Demo dumps")
j = json.dumps(data)
print(j)
print(data)

print('#'*50)
print("Demo dump")
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

print('#'*50)
print("Demo indent")
j = json.dumps(data, indent=4)
print(j)

print('#'*50)
print("Demo compact separator")
j = json.dumps(data, separators=(",", ":"), indent=4)
print(j)

print('#'*50)
print("Demo loads")
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(json_string)
print(data)
print(type(json_string))
print(type(data))

print('#'*50)
print("Demo load")
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print('#'*50)
print("Demo jsonplaceholder")
res = requests.get("https://jsonplaceholder.typicode.com/todos")
print(res.json())
x=json.loads(res.text)
print(x)
print(type(res.json()))
print(type(x))

print('#'*50)
print("Demo Querying Json")
print("Count completed tasks by users")
res = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(res.text)
todos_by_user={}
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]]=1
print(todos_by_user)

print(sorted(todos_by_user.items(), key=lambda y: y[1]))

print('#'*50)
print("json input with multiple rows")
x = '[{"pink": false, "purple": true, "red": false}, {"pink": false, "purple": false, "red": false}]'
x = json.loads(x)
print(x)
for y in x:
    print(y["purple"])



