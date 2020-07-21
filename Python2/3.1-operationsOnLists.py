# This program counts how many characters totally in a list of strings

def total_length(given_list):
    count = 0
    for string in given_list:
        count += len(string)
    return count

# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 9:
print(total_length(['chocolate']))

# Should return 0 (it has 4 empty strings):
print(total_length(["", "", "", ""]))
