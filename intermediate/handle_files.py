import json

json_file = open('intermediate/new_file.json', 'r+')

json_test = {
    "name": "Santiago",
    "surname": "Arteche",
    "age": 25
}

json.dump(json_test, json_file, indent = 2)


json_dict = json.load(open('intermediate/new_file.json'))
print(json_dict)
json_dict['name'] = 'Daniel'
print(json_dict)


