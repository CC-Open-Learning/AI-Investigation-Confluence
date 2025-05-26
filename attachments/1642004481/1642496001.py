import json

# Writing to a JSON file
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded Data:", loaded_data)

# Reading and writing text files
with open('example.txt', 'w') as txt_file:
    txt_file.write("Hello, world!")

with open('example.txt', 'r') as txt_file:
    content = txt_file.read()
    print("Text File Content:", content)
