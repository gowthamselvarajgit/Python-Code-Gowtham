from logo import logo
from menu_data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def menu_print():
    for item in MENU:
        print(f"{item.title()} : ${MENU[item]['cost']}")

def display_report():
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    
    print(f"Water: {water_level}ml")
    print(f"Milk: {milk_level}ml")
    print(f"Coffee: {coffee_level}g")
    print(f"Money: ${money}")

def change_calculator(fifty_rupees, twenty_rupees, ten_rupees, five_rupees, user_request):
    total_rupees = (fifty_rupees * 50) + (twenty_rupees * 20) + (ten_rupees * 10) + (five_rupees * 5)
    global money

    print(f"You have inserted ₹{total_rupees}.")
    coffee_price = MENU[user_request]["cost"]
    money += coffee_price
    change = round(total_rupees - coffee_price, 2)

    if total_rupees >= coffee_price:
        return change
    else:
        return -1
    
def coffee_maker(user_request):
    water_needed = MENU[user_request]["ingredients"]["water"]
    milk_needed = MENU[user_request]["ingredients"]["milk"]
    coffee_needed = MENU[user_request]["ingredients"]["coffee"]

    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

    if water_needed > water_available or milk_needed > milk_available or coffee_needed > coffee_available:
        return False
    else:
        resources["water"] = resources["water"] - MENU[user_request]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[user_request]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[user_request]["ingredients"]["coffee"]
        return True
    
shutdown = False

while not shutdown:
    print(logo)
    menu_print()
    user_request = input("What would you like to order? (ESPRESSO/LATTE/CAPPUCCINO): ").lower()

    if user_request == "report":
        display_report()
    elif user_request == "off":
        shutdown = True
    elif user_request in MENU:
        print("Please insert rupees.")
        fifty_rupees = int(input("How many 50 rupees?: "))
        twenty_rupees = int(input("How many 20 rupees?: "))
        ten_rupees = int(input("How many 10 rupees?: "))
        five_rupees = int(input("How many 5 rupees?: "))

        change = change_calculator(fifty_rupees, twenty_rupees, ten_rupees, five_rupees, user_request)
        if change == -1:
            print("Sorry that's not enough money. Money refunded.")
        elif change > 0:
            print(f"Here is ₹{change} in change.")
        elif change == 0:
            print("No change.")

        coffee_status = coffee_maker(user_request)
        if coffee_status == False:
            print("Sorry, not enough resources to make your coffee.")
        else:
            print(f"Here is your {user_request}. Enjoy!")
    else:
        print("Invalid input. Please try again.")





