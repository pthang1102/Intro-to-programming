# Several built-in methods on Lists:

# 1. append: adds its arguments as a SINGLE ITEM to the end of the list.
# It only ever adds ONE item to a list.
list1 = [1, 2, 3]
list1.append([4, 5, 6])
print(list1) # Should print [1, 2, 3, [4, 5, 6]]

list2 = [1, 2, 3]
list2.append("abc")
print(list2) # Should print [1, 2, 3, 'abc']

#2. extend: treats its argument as a sequence and adds each item in the
# sequence to the end of the list. In other words, it adds a sequence
# of items to a list.
list3 = [1, 2, 3]
list3.extend([4, 5, 6])
print(list3) # Should print [1, 2, 3, 4, 5, 6]

list4 = [1, 2, 3]
list4.extend("abc")
print(list4) # Should print [1, 2, 3, 'a', 'b', 'c']

# 3. sort: change a list so it is in alphabetical (and numerical) order.
# 4. reverse: change a list so it is in the opposite order from how it was before.