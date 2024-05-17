MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}


def print_report():
    """Print a report of the resources available."""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")
    print()

def check_resources(order):
    """Checks if there are enough resources to make the coffee."""
    valid_resources = True
    order_ingredients = MENU[order]["ingredients"]
    for ingredient in order_ingredients:
        required_resource = MENU[order]["ingredients"][ingredient]
        if required_resource > resources[ingredient]:
            valid_resources
            print(f"Sorry there is not enough {ingredient}.")
            valid_resources = False
            return valid_resources
    return valid_resources
        
        
def process_coins():
    """Processes the number of coins entered."""
    paid = 0
    coins = {"quarters":0.25, "dimes":0.1, "nickles":0.05, "pennies":0.01}
    for coin in coins:
        entered = int(input(f"How many {coin}?: "))
        paid += entered * coins[coin]
    return paid
    

def check_transaction(order, paid):
    """Check if the transaction was successul. Return change or add money to coffers."""
    price = MENU[order]["cost"]
    if paid < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif paid > price:
        change = round((paid - price), 2)
        print(f"Here is your change: ${change}")
        resources["money"] += price
        return True
    else:
        resources["money"] += price
        return True

def make_coffee(order):
    """Make the coffee ordered and subtract the required ingredients."""
    order_ingredients = MENU[order]["ingredients"]
    for ingredient in order_ingredients:
        ingredient_amount = MENU[order]["ingredients"][ingredient]
        resources[ingredient] -= ingredient_amount
    print(f"Here is your: {order}, enjoy!")
    print()


on = True
while on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        on = False
    elif order == "report":
        print_report()
    else:
        in_stock = check_resources(order)
        if in_stock:
            paid = process_coins()
            valid_transaction = check_transaction(order, paid)
            if valid_transaction:
                make_coffee(order)

    


