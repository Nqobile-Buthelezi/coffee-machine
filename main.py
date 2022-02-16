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

money = {
    "money": 0
}

hot_beverage = "☕"

is_on = True

espresso_product = MENU["espresso"]["ingredients"]
latte_product = MENU["latte"]["ingredients"]
cappuccino_product = MENU["cappuccino"]["ingredients"]

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

quarters = 0.25
dimes = 0.10
pennies = 0.01
nickels = 0.05


def give_a_report():
    """Returns a detailed report of all resources held within the coffee machine."""
    statement = f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\n" \
                f"money: ${money['money']}"
    return statement


def sufficient_resources(product_milk, product_water, product_coffee):
    """Returns a true statement if the resources to make a product are available and, returns a statement depending
    on what is lacking or insufficient. """
    if product_water <= resources['water']:
        if product_milk < resources['milk']:
            if product_coffee < resources['coffee']:
                return True
            elif product_coffee > resources['coffee']:
                return False
        elif product_milk > resources['milk']:
            return False
    elif product_water > resources['water']:
        return False


def calculate_cost(total_quarters, total_dimes, total_nickels, total_pennies):
    total_input = (total_quarters * quarters) + (total_dimes * dimes) + (total_nickels * nickels) + (
                total_pennies * pennies)
    return total_input


# TODO 3: The prompt should show every time the action has completed, e.g. once the drink is dispensed. The prompt
#  should show again to serve the next customer.
while is_on:
    # TODO 1: Prompt the user by asking them "What would you like? (espresso,latte,cappuccino):"
    order = input("What would you like? (espresso,latte,cappuccino): ")

    # TODO 2: Check the user's input to decide what to do next.
    if order == "espresso":
        if sufficient_resources(
                product_water=espresso_product["water"],
                product_coffee=espresso_product["coffee"],
                product_milk=0):
            number_of_quarters = float(input("How many quarters? "))
            number_of_dimes = float(input("How many dimes? "))
            number_of_nickels = float(input("How many nickels? "))
            number_of_pennies = float(input("How many pennies? "))

            user_coins = calculate_cost(number_of_quarters, number_of_dimes, number_of_nickels, number_of_pennies)

            if user_coins > espresso_cost:
                resources["water"] -= espresso_product["water"]
                resources["coffee"] -= espresso_product["coffee"]
                resources["milk"] -= 0
                money["money"] += espresso_cost
                refund = user_coins - espresso_cost
                print(f"Here's your change ${refund}.")
            else:
                print("You don't have enough money to purchase this, you have been refunded.")
        else:
            print("The resources to make this drink are insufficient.")
    elif order == "latte":
        if sufficient_resources(
                product_water=latte_product["water"],
                product_coffee=latte_product["coffee"],
                product_milk=latte_product["milk"]):
            number_of_quarters = float(input("How many quarters? "))
            number_of_dimes = float(input("How many dimes? "))
            number_of_nickels = float(input("How many nickels? "))
            number_of_pennies = float(input("How many pennies? "))

            user_coins = calculate_cost(number_of_quarters, number_of_dimes, number_of_nickels, number_of_pennies)

            if user_coins > latte_cost:
                resources["water"] -= latte_product["water"]
                resources["coffee"] -= latte_product["coffee"]
                resources["milk"] -= latte_product["milk"]
                money["money"] += latte_cost
                refund = user_coins - latte_cost
                print(f"Here's your change ${refund}.")
            else:
                print("You don't have enough money to purchase this, you have been refunded.")
        else:
            print("The resources to make this drink are insufficient.")
    elif order == "cappuccino":
        if sufficient_resources(
                product_water=cappuccino_product["water"],
                product_coffee=cappuccino_product["coffee"],
                product_milk=cappuccino_product["milk"]):
            number_of_quarters = float(input("How many quarters? "))
            number_of_dimes = float(input("How many dimes? "))
            number_of_nickels = float(input("How many nickels? "))
            number_of_pennies = float(input("How many pennies? "))

            user_coins = calculate_cost(number_of_quarters, number_of_dimes, number_of_nickels, number_of_pennies)

            if user_coins > cappuccino_cost:
                resources["water"] -= cappuccino_product["water"]
                resources["coffee"] -= cappuccino_product["coffee"]
                resources["milk"] -= cappuccino_product["milk"]
                money["money"] += cappuccino_cost
                refund = user_coins - cappuccino_cost
                print(f"Here's your change ${refund}.")
            else:
                print("You don't have enough money to purchase this, you have been refunded.")
        else:
            print("The resources to make this drink are insufficient.")
    # TODO 4: Turn off the Coffee Machine by entering “ off ” to the prompt. For maintainers of the coffee machine,
    #  they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
    elif order == "off":
        print("The machine is powering down.")
        is_on = False
    # TODO 5: When the user enters “report” to the prompt, a report should be generated that shows the current
    #  resource values.
    elif order == "report":
        print(give_a_report())
    else:
        print("I'm sorry we don't have that in stock.")
