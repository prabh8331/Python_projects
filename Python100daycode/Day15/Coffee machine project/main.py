MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# #[ ] 2. Check resources sufficient?
#     print("Sorry there is not enough water") # if milk/5 is not sufficient print that

def check_resources(choice_input):
    """Check if Resources are sufficient"""
    sufficient = True
    if resources["water"] < MENU[choice_input]["ingredients"]['water']:
        print("Sorry there is not enough water")
        sufficient = False
    if resources["milk"] < MENU[choice_input]["ingredients"]['milk']:
        print("Sorry there is not enough milk")
        sufficient = False
    if resources["coffee"] < MENU[choice_input]["ingredients"]['coffee']:
        print("Sorry there is not enough coffee")
        sufficient = False
    return sufficient


# #[ ] 3. Process coins 
#     # when user give the input of drink it should ask insert coins 
#     print("Please insert coins.")
#     #How many quatres?: 
#     #How many dimes?: 
#     #How many nickles?:     
#     #How many pennies?: 
#     # values - quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#     # if money is not enough to buy the drink
#     print("Sorry that's not enough money. Money refunded")

def coin_process():
    """Allow user to input coins in the machine"""
    print("Please insert coins.")
    quatres = int(input("How many quatres?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quatres * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

# #[ ] 4. Check transaction successful?
#     # if enough money and resources print : 
#     # then make the coffee and deduct the resources 
#     # Here is your espresso ☕ Enjoy!


def transaction(resources_input, choice_input):
    """If Transaction the make the drink and deduct the resources and money"""
    water = resources_input["water"] - MENU[choice_input]["ingredients"]['water']
    milk = resources_input["milk"] - MENU[choice_input]["ingredients"]['milk']
    coffee = resources_input["coffee"] - MENU[choice_input]["ingredients"]['coffee']
    print(f"Here is your {choice_input}")
    return {"water": water, "milk": milk, "coffee": coffee}


# TODO: Program requirements 
# print("What would you like? (espresso/latte/cappuccino)") # input
# [x] 1. Print report - this will tell how much resources has left (water,milk,coffee,money)
#    # if user give input of report then show 
#    # Water: 100ml 
#    # Milk: 50ml 
#    # Coffee: 76g 
#    # Money: $2.5
money = 0

CONTINUE_MACHINE = True

while CONTINUE_MACHINE:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(choice):
            money += coin_process()
            if money >= MENU[choice]["cost"]:
                money -= MENU[choice]["cost"]
                resources = transaction(resources, choice)
            else:
                print("Sorry that's not enough money. Money refunded")
    elif choice == "off":
        CONTINUE_MACHINE = False
    else:
        print("Error: Invalid input!")
