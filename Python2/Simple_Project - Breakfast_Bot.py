# This program allows customers to order simple breakfasts.
# It also validates user inputs.
import time


# Print Introduction
def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.\n")
    print_pause("Today we have two breakfasts available.\n")
    print_pause("The first is waffles with strawberries and whipped cream.\n")
    print_pause("The second is sweet potato pancakes with butter and syrup.\n")


# Print the message and pause 2 seconds after printing
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Validate user input
def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand.")


# Get order from customers
def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           ["waffles", "pancakes"])
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()


# Check if customers want to order again
def order_again():
    response = valid_input("Would you like to place another order? "
                           "Please say 'yes' or 'no'.\n",
                           ["yes", "no"])
    if 'no' in response:
        print_pause("OK, goodbye!")
    elif 'yes' in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()


# UI
def order_breakfast():
    intro()
    get_order()


# Program starts here
order_breakfast()
