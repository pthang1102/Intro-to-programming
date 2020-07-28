# This function checks if a string is a substring of another
def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            return True
        index += 1
    return False

print(is_substring('day', 'wednesday')) # Return True
print(is_substring('tablet', 'table tennis')) # Return False 