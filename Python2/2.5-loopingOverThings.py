# Loop and print characters from a string entered by user
message = input("What do you want to print?")

for ch in message:
    print(ch)
    if ch == "?":
        print("Sense much curiousity in you, I do.")
    if ch == "!":
        print("Enthusiastic, you are.")
