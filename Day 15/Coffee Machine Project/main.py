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
    """
    Prints the current status of the coffee machine.

    Displays the remaining quantities of water, milk, and coffee,
    as well as the total amount of money collected.
    Initializes the money resource to 0 if it does not exist.
    """
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
    if "money" not in resources:
        resources["money"] = 0
    print("Money: ", resources["money"])


def check_resource_sufficieny(coffee_type):
    """
    Checks whether the machine has enough ingredients
    to prepare the selected coffee.

    Args:
        coffee_type (str): The selected coffee type.

    Returns:
        str: "enough" if all required ingredients are available,
             otherwise "not enough".
    """
    if coffee_type == "cappuccino" or coffee_type == "latte":
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


def insert_coins(coffee_type):
    """
    Handles the payment process for the selected coffee.

    Collects coins from the customer, calculates the total
    payment, compares it with the coffee price, calculates
    change if necessary, and updates the machine's money balance.

    If payment is sufficient, calls deduct_ingredients()
    to update the available resources.

    Args:
        coffee_type (str): The selected coffee type.
    """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_sum_paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    cost_of_coffee = MENU[coffee_type]["cost"]
    if total_sum_paid >= cost_of_coffee:
        change = total_sum_paid - cost_of_coffee
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += cost_of_coffee
        print("Money is $", resources["money"])
        deduct_ingredients(coffee_type=coffee_type)
        print(f"Here is your {coffee_type}. Enjoy!")
    elif total_sum_paid < cost_of_coffee:
        print("Total inserted money: $", round(total_sum_paid, 2))
        print("Sorry that's not enough money. Money refunded.")


def deduct_ingredients(coffee_type):
    """
    Deducts the required ingredients from the machine's resources
    after a successful coffee purchase.

    Retrieves the ingredient quantities from MENU, subtracts
    them from the available resources, and prints an updated report.

    Args:
        coffee_type (str): The selected coffee type.
    """
    if coffee_type == "cappuccino" or coffee_type == "latte":
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
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_request == "report":
        print_report()

    elif user_request == "off":
        print("Coffee machine is off.")
        is_machine_off = True

    elif user_request == "latte":
        resource = check_resource_sufficieny("latte")
        if resource == "enough":
            insert_coins("latte")
    elif user_request == "cappuccino":
        resource = check_resource_sufficieny("cappuccino")
        if resource == "enough":
            insert_coins("cappuccino")
    elif user_request == "espresso":
        resource = check_resource_sufficieny("espresso")
        if resource == "enough":
            insert_coins("espresso")
