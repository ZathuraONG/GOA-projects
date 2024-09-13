#task 1
table = {
    "dog": "white",
    "cat": "black",
    "car": "blue"
}

for key in table:
    value = table[key]
    print(key)
    print(value)

print(table["dog"])
print(table["cat"])
print(table["car"])

#task 2

for key, value in table.items():
    print(key)
    print(value)

#task 3

table2 = {
    "fruits": ["apple", "banana", "cherry"],
    "colors": ["red", "green", "blue"],
    "animals": ["dog", "cat", "bird"]
}

#task 4


table4 = {
    "table5": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
}