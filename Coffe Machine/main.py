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


def check_resources(answer):
    if resources["water"] < MENU[answer]["ingredients"]["water"]:
        return False
    if resources["milk"] < MENU[answer]["ingredients"]["milk"]:
        return False
    if resources["coffee"] < MENU[answer]["ingredients"]["coffee"]:
        return False
    return True


def ask_for_money(answer):
    print("Please enter money in the coffee machine")
    ans_quarters = int(input("How many Quarters you're entering? "))
    ans_dimes = int(input("How many Dimes you're entering? "))
    ans_nickles = int(input("How many Nickles you're entering? "))
    ans_pennies = int(input("How many Pennies you're entering? "))

    total = 0.25*ans_quarters + 0.1*ans_dimes + 0.05*ans_nickles + 0.01*ans_pennies
    if total >= MENU[answer]["cost"]:
        print(f"Here is your change ${round(total-MENU[answer]["cost"],2)}")
        return True
    else:
        print("The money entered was not enough. Please try again")
        return False


def deduct_from_resources(answer):
    resources["water"] -= MENU[answer]["ingredients"]["water"]
    resources["milk"] -= MENU[answer]["ingredients"]["milk"]
    resources["coffee"] -= MENU[answer]["ingredients"]["coffee"]


def start_machine():
    answer = input("What do you want to have:(Espresso/Latte/Cappuccino) ").lower()
    if answer == "espresso":
        if check_resources(answer):
            if not ask_for_money(answer):
                start_machine()
            else:
                print(f"Here is your {answer}")
                deduct_from_resources(answer)
        else:
            print("Insufficient Ingredients! Sorry!")
    elif answer == "latte":
        if check_resources(answer):
            if not ask_for_money(answer):
                start_machine()
            else:
                print(f"Here is your {answer}")
                deduct_from_resources(answer)
        else:
            print("Insufficient Ingredients! Sorry!")
    elif answer == "cappuccino":
        if check_resources(answer):
            if not ask_for_money(answer):
                start_machine()
            else:
                print(f"Here is your {answer}")
                deduct_from_resources(answer)
        else:
            print("Insufficient Ingredients! Sorry!")
    elif answer == "report":
        print(f"Water left if {resources["water"]}")
        print(f"Milk left if {resources["milk"]}")
        print(f"Coffee left if {resources["coffee"]}")
    ans = input("Do you want anything else:(yes/no) ").lower()
    if ans == "yes":
        start_machine()


if __name__ == '__main__':
    print("Hello There! This is your personal virtual coffee machine.")
    start_machine()
    print("See you soon")