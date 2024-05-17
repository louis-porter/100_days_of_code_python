from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


on = True
while on:
    order = input(f"What would you like to order? {menu.get_items()}: ")
    if order == "off":
        on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            paid = money_machine.make_payment(drink.cost)
            if paid:
                coffee_maker.make_coffee(drink)

            
            



            






