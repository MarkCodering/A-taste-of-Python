"""
File IO in Python
"""
import json

contents = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("./files.json", "w", encoding="UTF-8") as file:
    json.dump(contents, file, indent=4)

# Path: src/files.json
with open("./files.json", "r", encoding="UTF-8") as file:
    contents = json.load(file)
    print(contents)

    file.close()