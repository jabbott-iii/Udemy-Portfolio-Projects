from importlib import resources

resources = {}
resources["water"] = 300
resources["milk"] = 200
resources["coffee"] = 100

coffee_list = [
    {
        "name": "espresso",
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5,
    },
    {
        "name": "latte",
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    {
        "name": "cappuccino",
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    },

]

def get_coffee_coins():
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    total = 0
    print("Please insert coins.")
    for coin, value in coins.items():
        count = int(input(f"How many {coin}?: "))
        total += count * value
    return total

def check_resources(drink, resources):
    """Returns True if there are enough resources to make the drink, return False otherwise."""
    for item in ["water", "milk", "coffee"]:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}. Contact maintenance.")
            return False
    resources["water"] -= drink["water"]
    resources["milk"] -= drink["milk"]
    resources["coffee"] -= drink["coffee"]
    print("Resources remaining are: ", resources)
    return True