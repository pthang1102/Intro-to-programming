# This function locates and returns the position(s) of a substring in a string.
def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index:index+len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

print(locate_all('cookbook', 'ook')) # [1, 5]
print(locate_all('yesyesyesyes', 'yes')) # [0, 3, 6, 9]
print(locate_all('helsinki', 'finland')) # []