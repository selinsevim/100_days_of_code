


# TODO 4: Check resources sufficient?
# TODO 5: Process coins - If there are sufficient resources to make the drink selected, 
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
    }
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


is_machine_off = False

# while there is enough resources, run the coffee machine
while not resources["water"] == 0 and not resources["milk"] == 0 and not resources["coffee"] == 0 and not is_machine_off:
    
    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 3: Print report - how much milk, coffee etc
    if user_request == "report":
      print_report()

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt. - code should stop executing
    elif user_request == "off":
       print("Coffee machine is off.")
       is_machine_off = True
       

    
       