from coffee_data import coffee_menu

profit = 0
resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}


def report(left_resources, total_profit):
    """Generate report based on left resources and total profit"""
    print(f"Water: {left_resources['water']}ml\nMilk: "
          f"{left_resources['milk']}ml\nCoffee: {left_resources['coffee']}g\n"
          f"Money: ${total_profit}")


def user_money(quarters, dimes, nickles, pennies):
    """Calculates total amount of money inserted by a user"""
    total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + \
                   0.01 * pennies
    return total_amount


def user_coffee(user_choice):
    """Gets full info about user choice and returns it"""
    for i in coffee_menu:
        if i['coffee_type'] == user_choice:
            user_coffee = i
            return user_coffee


def is_transaction_successful(total_user_amount, cost):
    """Calculates if sum inserted by a user is sufficient
    and return True if yes, and False if no"""
    if total_user_amount > cost:
        change = round(total_user_amount - cost, 2)
        print(f"Here is ${change} dollars in change")
        return True
    elif total_user_amount == cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def is_resources_enough(resources, user_coffee):
    """Calculates if resourses is enough and returns True if yes and False"""
    left_resources = resources.copy()
    for key in left_resources:
        left_resources[key] = left_resources[key] - user_coffee[key]
        if left_resources[key] < 0:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def interaction(resources, user_coffee, profit):
    if is_resources_enough(resources, user_coffee):
        user_quarters = int(input("Please insert money!\nQuarters: "))
        user_dimes = int(input("Dimes: "))
        user_nickles = int(input("Nickles: "))
        user_pennies = int(input("Pennies: "))
        total_user_amount = user_money(user_quarters, user_dimes, user_nickles,
                                       user_pennies)
        if is_transaction_successful(total_user_amount, user_coffee["cost"]):
            for key in resources:
                left_resources[key] = resources[key] - user_coffee[key]
            total_profit = profit + user_coffee["cost"]
            print(f"Here is your {user_coffee['coffee_type']}! Enjoy ☕️  ")
            return left_resources, total_profit
        else:
            return resources, profit
    else:
        return resources, profit


left_resources = resources
total_profit = profit

while True:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino) or report: ")
    if user_choice == 'espresso' or user_choice == 'latte' or \
            user_choice == 'cappuccino':
        selected_coffee = user_coffee(user_choice)
        left_resources, total_profit = interaction(left_resources,
                                                   selected_coffee,
                                                   total_profit)
    elif user_choice == 'report':
        report(left_resources, total_profit)
    elif user_choice == 'off':
        exit()



