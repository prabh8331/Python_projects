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

#TODO: Program requirements 
print("What would you like? (espresso/latte/cappuccino)") # input
#[ ] 1. Print report - this will tell how much resources has left (water,milk,coffee,money)
    # if user give input of report then show 
    # Water: 100ml 
    # Milk: 50ml 
    # Coffee: 76g 
    # Money: $2.5
#[ ] 2. Check resources sufficient?
    print("Sorry there is not enough water") # if milk/coffee is not sufficient print that

#[ ] 3. Process coins 
    # when user give the input of drink it should ask insert coins 
    print("Please insert coins.")
    #How many quatres?: 
    #How many dimes?: 
    #How many nickles?:     
    #How many pennies?: 
    # values - quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # if money is not enough to buy the drink
    print("Sorry that's not enough money. Money refunded")


#[ ] 4. Check transaction successful?
    # if enough money and resources print : 
    # then make the coffee and deduct the resources 
    # Here is your espresso ☕ Enjoy!

# use to do list to breakdown of code 