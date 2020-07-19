# Testing with function 'len'

def too_long(s):
    return len(s) > 140

print("This should be False:")
print(too_long("I am a short string!"))