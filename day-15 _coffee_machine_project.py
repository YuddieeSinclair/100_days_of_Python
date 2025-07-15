#WELCOME TO THE COFFEE MACHINE

option = True
quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01


water = 1000
milk = 500
coffee = 300
money = 0

espresso = 1.50
latte = 2.50
cappuccino = 3.00

while option:
    user_input = input("What would you like to? (espresso/latte/cappuccino): ")

    if user_input == "espresso":
        if water >= 50:
            if coffee >= 18:
                quarter_input = int(input('how many quarters: '))
                dime_input = int(input('how many dimes: '))
                nickel_input = int(input('how many nickels: '))
                penny_input = int(input('how many pennies: '))
                water -= 50
                coffee -= 18
                milk -= 0 #Espresso does not require milk
                total = (quarter_input * quarter) + (dime * dime_input) + (nickel_input * nickle) + (penny_input * penny)
                if total == espresso:
                    money += total
                elif total >= espresso:
                    change = total - espresso
                    money += espresso
                    print("Enjoy your espresso!")
                    print(f'here is your change: ${round(change, 2)}')
                else:
                    print('not enough cash')
            else:
                 print("sorry there is not enough Coffee")
        else:
             print("sorry there is not enough water")
    elif user_input == "latte":
        if water >= 200:
            if coffee >= 24:
                if milk >= 150:
                    quarter_input = int(input('how many quarters: '))
                    dime_input = int(input('how many dimes: '))
                    nickel_input = int(input('how many nickels: '))
                    penny_input = int(input('how many pennies: '))
                    water -= 200
                    coffee -= 24
                    milk -= 150
                    # latte = 2.50$
                    total = (quarter_input * quarter) + (dime * dime_input) + (nickel_input * nickle) + (penny_input * penny)
                    if total == latte:
                        money += total
                    elif total >= latte:
                        change = total - latte
                        money += latte
                        print("Enjoy your latte!")
                        print(f'here is your change: ${round(change, 2)}')
                    else:
                        print('not enough cash')
                else:
                     print("sorry there is not enough milk")
            else:
                 print("sorry there is not enough Coffee")
        else:
             print("sorry there is not enough water")
    elif user_input == "cappuccino":
         if water >= 250:
            if coffee >= 24:
                if milk >= 100:
                    quarter_input = int(input('how many quarters: '))
                    dime_input = int(input('how many dimes: '))
                    nickel_input = int(input('how many nickels: '))
                    penny_input = int(input('how many pennies: '))
                    water -= 250
                    coffee -= 24
                    milk -= 100
                    total = (quarter_input * quarter) + (dime * dime_input) + (nickel_input * nickle) + (penny_input * penny)

                    if total == cappuccino:
                        money += total
                    elif total >= cappuccino:
                        change = total - cappuccino
                        money += cappuccino
                        print("Enjoy your cappuccino!")
                        print(f'here is your change: ${round(change, 2)}')
                    else:
                        print('not enough cash')
                else:
                     print("sorry there is not enough milk")
            else:
                 print("sorry there is not enough Coffee")
         else:
             print("sorry there is not enough water")
    elif user_input == "off":
        option = False
    elif user_input == "report":
        print(f"Water:{water}\nmilk:{milk}\nCoffee:{coffee}\nmoney:{money}")
    else:
        print("choose a correct option")