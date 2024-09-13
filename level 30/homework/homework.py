#task2
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

#task 3

cars = {
    "Car1": {
        "Make": "Toyota",
        "Model": "Camry",
        "Year": 2021,
        "Price": "$24,000"
    },
    "Car2": {
        "Make": "Honda",
        "Model": "Civic",
        "Year": 2022,
        "Price": "$22,000"
    },
    "Car3": {
        "Make": "Ford",
        "Model": "Mustang",
        "Year": 2020,
        "Price": "$30,000"
    }
}

for car, info in cars.items():
    print(f"Introducing {car} for sale!")
    print(f"Make: {info['Make']}")
    print(f"Model: {info['Model']}")
    print(f"Year: {info['Year']}")
    print(f"Price: {info['Price']}")
    print("------------") #uketesad dasanaxi rom iyos
