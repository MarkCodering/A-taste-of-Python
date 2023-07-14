dictionary = {
    "name": "Seth",
    "age": 20,
    "hobbies": ["coding", "gaming", "reading"],
}

print(dictionary["name"])

# Add a new key-value pair
dictionary["gender"] = "male"
for key in dictionary:
    print(key, dictionary[key])