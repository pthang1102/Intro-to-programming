# This program gives users a ride in its 3-floor elevator.
# Choose which floor do you want to go to, and see what happens!
# You are a programming engineer coming to your new workplace the 1st time!
# Let's discover!

import time


# Print the message and pause 1 second after printing
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# Print Introduction
def intro():
    print_pause("You have just arrived at your new job!\n")
    print_pause("You are in the elevator.\n")


# What happens in the 1st floor
def first_floor(items):
    print_pause("You push the button for the first floor.\n")
    print_pause("After a few moments, you find yourself in the lobby.\n")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.\n")
    else:
        print_pause("The clerk greets you and gives you your ID card.\n")
        items.append("ID card")

    print_pause("Where would you like to go next?\n")
    elevator(items)


# What happens in the 2nd floor
def second_floor(items):
    print_pause("You push the button for the second floor.\n")
    print_pause("After a few moments, you find yourself in "
                "the human resources department.\n")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.\n")
        print_pause("There doesn't seem to be much to do here.\n")
    else:
        print_pause("The head of HR greets you.\n")
        if "ID card" in items:
            print_pause("He looks at your ID card and then gives you "
                        "a copy of the employee handbook.\n")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.\n")
    print_pause("Where would you like to go next\n")
    elevator(items)


# What happens in the 3rd floor
def third_floor(items):
    print_pause("You push the button for the third floor.\n")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.\n")
    print_pause("This is where you work!\n")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.\n")
        print_pause("Your program manager greets you.\n")
        print_pause("She tells you that you need to have "
                    "a copy of the employee handbook in order to "
                    "start work.\n")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!\n")
            print_pause("Congratulations! You are ready to start your new "
                        "jobs as vice president of engineering!\n")
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.\n")
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.\n")
        print_pause("It looks like you need some kind of key "
                    "to open the door.\n")
        print_pause("You head back to the elevator.\n")
    print_pause("Where would you like to go next?\n")
    elevator(items)


# Operate the elevator
def elevator(items):
    response = input("Please enter the number for the floor "
                     "you would like to visit:\n"
                     "1. Lobby\n"
                     "2. Human resources.\n"
                     "3. Engineering department.\n")
    if response == "1":
        first_floor(items)
    elif response == "2":
        second_floor(items)
    elif response == "3":
        third_floor(items)
    # Handle incorrect user input
    else:
        print_pause("I don't understand your input.")
        elevator(items)


# UI
def play_game():
    items = []
    intro()
    elevator(items)


# Start program
play_game()
