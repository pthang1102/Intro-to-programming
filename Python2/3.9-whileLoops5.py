# This program takes a string argument and 
# prints the portion of that string before the first dot (.) character.

def until_dot(str):
    index = 0
    while index < len(str) and str[index] != ".":
        index += 1
    print(str[:index])

until_dot("This is a sentence, print this. This is another.")
until_dot("192.168.1.1")