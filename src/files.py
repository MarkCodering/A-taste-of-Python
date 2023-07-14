import json

contents = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("./files.json", "w") as file:
    json.dump(contents, file, indent=4)

# Path: src/files.json
with open("./files.json", "r") as file:
    contents = json.load(file)
    print(contents)