import json

result = {
  "1": [True, 1625420535.8975282, "Car"],
  "2": [False, 1625420535.8975282, None],
  "3": [True, 1625420535.8975282, "Car"],
  "4": [True, 1625420535.8975282, "Truck"],
  "5": [False, 1625420535.8975282, None],
  "6": [True, 1625420535.8975282, "Truck"],
  "7": [False, 1625420535.8975282, None],
  "8": [False, 1625420535.8975282, None]
}

with open("data.json", "w") as f:
    json.dump(result, f)
  