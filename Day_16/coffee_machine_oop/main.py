from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# CoffeeMaker has report, is_resource_enough, make_coffee methods and resources attributes
# Menu has get_items, find_drink methods
# MoneyMachine has report, process_coins, make_payments methods and

is_machine_off = False

# Define the objects
make_coffee = CoffeeMaker()
menu_opt = Menu()
money_opt = MoneyMachine()

print(menu_opt.find_drink("latte"))

while not is_machine_off:
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_request == "report":
        make_coffee.report()
    elif user_request == "latte":
        latte = menu_opt.find_drink("latte")
        print("latte ingredients are", latte.ingredients)
        if latte:
            if make_coffee.is_resource_sufficient(latte):
                money_opt.process_coins()
