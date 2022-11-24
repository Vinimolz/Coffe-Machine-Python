from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like to order ? ({options})")

    if user_choice == "off":
        is_on = False
    # print report
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # check resources
        drink = menu.find_drink(user_choice)
        # process coins check transaction
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # make coffee and deduct from ingredients
            coffee_maker.make_coffee(drink)