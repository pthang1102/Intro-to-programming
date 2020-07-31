# This simple game gives user some options.
# Read, choose wisely for winning the game.

import time
import random

# Print, then pause 1 second after printing
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# Print Introduction
def intro(items, monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + monster + " is somewhere "
                "around here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


# On the field
def field(items, monster):
    print_pause("Enter [1] to knock on the door of the house.\n")
    print_pause("Enter [2] to peer into the cave.\n")
    print_pause("What would you like to do?\n")
    
    choice = input("Please enter [1] or [2]:\n")
    if choice == "1":
        house(items, monster)
    elif choice == "2":
        cave(items, monster)
    else:
        print_pause("Wrong input! Please enter again!")
        field(items, monster)


# When player chooses to explore the cave
def cave(items, monster):
    print_pause("You peer cautiously into the cave.\n")
    if "sward" in items:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.\n")
    else:
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!!!\n")
        print_pause("You discard your silly old dagger "
                    "and take the legendary sword with you!\n")
        items.append("sward")
    print_pause("You walk back to the field.\n")
    field(items, monster)


# When player chooses to check the house
def house(items, monster):
    print_pause("You approach the door of the house.\n")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a {monster}.\n")
    print_pause(f"Eep! This is the {monster}'s house!\n")
    print_pause(f"The {monster} attacks you!\n")
    if "sward" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "having only a tiny dagger.\n")
    while True:
        choice = input("Enter [1] to fight or [2] to run away.\n")
        if choice == "1":
            if "sward" in items:
                print_pause(f"As the {monster} moves to attack, "
                            "you unsheath your new sword.\n")
                print_pause("The Sword of Ogoroth shines brightly in your "
                            "hand as you brace yourself for the attack.\n")
                print_pause(f"But the {monster} takes one look at "
                            "your shiny new weapon and runs away!\n")
                print_pause(f"You have rid the town of the {monster} "
                            "You are victorious!\n")
            else:
                print_pause("You do your best...\n")
                print_pause(f"but your dagger is no match for the {monster}.\n")
                print_pause("You have been defeated!\n")
            play_again()
            break
        elif choice == "2":
            print_pause("You run back into the field.\n")
            print_pause("Luckily, you don't seem to have been followed.\n")
            field(items, monster)
            break
        else:
            print_pause("Wrong input! Please enter again!\n")


# Play the game again
def play_again():
    response = input("Would you want to play again (y/n)?\n").lower()
    if response == "y":
        print_pause("Great!! Restarting the game ..\n")
        play_game()
    elif response == "n":
        print_pause("Hope you have a good time! See you next time!\n")
    else:
        print_pause("Wrong input! Please enter again!\n")
        play_again()


def play_game():
    items = []
    monsters = ["pirate", "dragon", "troll", "witch", "wicked fairy",
                "bandit", "big-bad-wolf"]
    monster = random.choice(monsters)
    intro(items, monster)
    field(items, monster)


# Start game!
play_game()
    