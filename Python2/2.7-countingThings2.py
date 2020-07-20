# Create a function to count how many 'given character' there are in a string
def count_character(str, ch):
    count = 0
    for char in str:
        if char == ch:
            count += 1
    return count

print("Should print a count of 3:")
print(count_character("Hello World!", "l"))

print("Should print a count of 0:")
print(count_character("that letter isn't here", "z"))
