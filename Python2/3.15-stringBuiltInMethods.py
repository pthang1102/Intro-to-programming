# Several popular String built-in methods

# in/not in
print(3 in [1, 2, 3, 4]) # True
print([2, 3] in [1, 2, 3, 4]) # False
print('food' in 'foodie') # True
print([2, 3] not in [1, 2, 3, 4]) # True

# find
print('abracadabra'.find('cad')) # Prints 4
print('abracadabra'.find('abcd')) # Prints -1

# count
print('love love love love, it is love'.count('love')) # Prints 5