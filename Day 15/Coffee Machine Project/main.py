# TODO 6: then the program should prompt the user to insert coins
# TODO 7: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 -> here calculate the money inserted
# TODO 8: Check transaction successful
# TODO 9: Make Coffee

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
    if "money" not in resources:
        resources["money"] = 0
    print("Money: ", resources["money"])


# TODO 4: Check resources sufficient?
def check_resource_sufficieny(coffee_type):
    if coffee_type == "cappuccino" and coffee_type == "latte":
        if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return "not enough"
        elif resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return "not enough"
        elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return "not enough"
        else:
            print("There is enough resources")
            return "enough"
    else:
        if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return "not enough"
        elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return "not enough"
        else:
            print("There is enough resources")
            return "enough"


# TODO 5: Process coins - If there are sufficient resources to make the drink selected,
def insert_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_sum_paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    cost_of_coffee = MENU[coffee_type]["cost"]
    if total_sum_paid > cost_of_coffee:
        change = total_sum_paid - cost_of_coffee
        print(f"Here is ${change} in change.")
        resources["money"] += cost_of_coffee
        print("Money is $", resources["money"])
        deduct_ingredients(coffee_type=coffee_type)
    elif total_sum_paid < cost_of_coffee:
        print(f"Total inserted money: $", total_sum_paid)
        print("Sorry that's not enough money. Money refunded.")


def deduct_ingredients(coffee_type):
    if coffee_type == "cappuccino" and coffee_type == "latte":
        resources["water"] = (
            resources["water"] - MENU[coffee_type]["ingredients"]["water"]
        )
        resources["coffee"] = (
            resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        )
        resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
        print_report()
    else:
        resources["water"] = (
            resources["water"] - MENU[coffee_type]["ingredients"]["water"]
        )
        resources["coffee"] = (
            resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        )
        print_report()


is_machine_off = False
resources["money"] = 0

# while there is enough resources, run the coffee machine
# while not resources["water"] == 0 and not resources["milk"] == 0 and not resources["coffee"] == 0 and not is_machine_off:
while not is_machine_off:
    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 3: Print report - how much milk, coffee etc
    if user_request == "report":
        print_report()

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt. - code should stop executing
    elif user_request == "off":
        print("Coffee machine is off.")
        is_machine_off = True

    elif user_request == "latte":
        resource = check_resource_sufficieny("latte")
        if resource == "enough":
            insert_coins("latte")
            print(f"Here is your latte. Enjoy!")
    elif user_request == "cappuccino":
        resource = check_resource_sufficieny("cappuccino")
        if resource == "enough":
            insert_coins("cappuccino")
            print(f"Here is your cappuccino. Enjoy!")
    elif user_request == "espresso":
        resource = check_resource_sufficieny("espresso")
        if resource == "enough":
            insert_coins("espresso")
            print(f"Here is your espresso. Enjoy!")
