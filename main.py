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

Money = 0

running = True




#todo 7. Make Coffee

def make_coffee(water, milk, coffee):
    resources["water"] = resources["water"] - water
    resources["coffee"] = resources["coffee"] - coffee
    resources["milk"] = resources["milk"] - milk
    print(f"Here is your {function}. Enjoy!☕")


# todo 4. Check resources sufficient?
def check_resource():
    c_water = MENU[function]["ingredients"]["water"]
    c_coffee = MENU[function]["ingredients"]["coffee"]
    c_milk = MENU[function]["ingredients"]["milk"]


    if resources["water"] - c_water >= 0 and resources["milk"] - c_milk >= 0 and resources["coffee"] - c_coffee >= 0:
        # check_transation()
        return (c_water, c_coffee, c_milk)

    elif resources["water"] - c_water < 0:
        print(f"Sorry, there is not enough water")
        return False

    elif resources["coffee"] - c_coffee < 0:
        print(f"Sorry, there is not enough coffee")
        return False

    elif resources["milk"] - c_milk < 0:
        print(f"Sorry, there is not enough milk")
        return False



#todo 5. Process coins.
#todo 6. Check transaction successful?

def process_coins():

    print("Please insert coins.")
    insert_coin_quarter = int(input("how many quarters?: "))
    insert_coin_dime = int(input("how many dimes?: "))
    insert_coin_nickle = int(input("how many nickles?: "))
    insert_coin_penny = int(input("how many pennies?: "))
    total_money = insert_coin_quarter * 0.25 + insert_coin_dime * 0.1 + insert_coin_nickle * 0.05 + insert_coin_penny * 0.01

    return total_money

def check_transation():
    current_money = check_resource()
    print(f"Here is {current_money} in change.")
    coffee_price = MENU[function]["cost"]

    if current_money-coffee_price>=0:
        return current_money
    else:
        return False


    # todo 3. Print report
def report():

    print(f"Water:{resources['water']}")
    print(f"Milk:{resources['milk']}")
    print(f"Coffee:{resources['coffee']}")
    print(f"Money:{Money}")




#todo 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#todo 2. Turn off the Coffee Machine by entering “off” to the prompt

while running == True:
    function = input("What would you like? (espresso/latte/cappuccino/report):")

    if function == "espresso" or function == "latte" or function == "cappuccino" :
        C = check_resource()

        # if C != False:
        #     C_T = check_transation()
        #     if C_T != False:
        #         make_coffee(check_resource())
        #         Money = Money + check_transation()
        #
        # else:
        #
        #     running = check_resource()

    elif function == "report":
        report()

    elif function == "off":
        running = False

    else:
        print("error")