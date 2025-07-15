#Welcome to the online Coffe Machine!
Menu = {
    "espresso":{
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "cost": 1.50
    },
    "latte":{
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.50
    },
    "cappuccino":{
        "water": 250,
        "coffee": 24,
        "milk": 100,
    }
}

Report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(user_input):
    if Report["water"] < drink["water"]:
        print("not enough water")
        return False
    elif Report["milk"] < drink["milk"]:
        print("not enough milk")
        return False
    elif Report["coffee"] < drink["coffee"]:
        print("not enough coffee")
        return False

def coin_procsess():
    drink = Menu[user_input]
    cash = 0
    quarter = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    cash += quarter +dimes + nickles + pennies
    if cash < drink["cost"]:
        print("not enough cash, here is your refund")
        return False
    elif cash > drink["cost"]:
        Report["money"] += drink["cost"]
        print(f"Here is your change: {round(cash - drink["cost"], 2)}$")
        print("enjoy your coffee")

def update(input):
    for key in Report:
       if not key == "money":
           Report[key] -= input[key]


while True:
    user_input = input("what would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        break
    elif user_input == "report":
        print(f"water: {Report["water"]}ml \nmilk: {Report["milk"]}ml \ncoffee: {Report["coffee"]}g \nmoney: {Report["money"]}$")
    elif user_input == "espresso":
        drink = Menu[user_input]
        if check_resources(drink) is False:
            continue
        print("kindly insert coins")
        coin_procsess()
        update(drink)
    elif user_input == "latte":
        drink = Menu[user_input]
        if check_resources(drink) is False:
            continue
        print("kindly insert coins")
        coin_procsess()
        update(drink)
    elif user_input == "cappuccino":
        drink = Menu[user_input]
        if check_resources(drink) is False:
            continue
        print("kindly insert coins")
        coin_procsess()
        update(drink)
    else:
        print("enter a valid option")