from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

report = coffee_maker.report()
cash = money_machine.report()



while True:
    user_input = input("what would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        break
    elif user_input == "report":
        print(f"{report}\n {cash}")
    else:
         drink = menu.find_drink(user_input)
         if coffee_maker.is_resource_sufficient(drink) is True:
             if money_machine.make_payment(drink.cost) is True:
                    coffee_maker.make_coffee(drink)
            
        
