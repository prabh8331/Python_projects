from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ask_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_on = True

while turn_on:
    choice = input(f"What would you like? ({ask_menu.get_items()}): ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        turn_on = False

    else:
        drink = ask_menu.find_drink(choice)
        if drink != None and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
