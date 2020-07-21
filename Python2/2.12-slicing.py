# Test several ways to slice a string

word = "university"
print(word[:3]) # Prints 'uni'
print(word[3:]) # Prints 'versity'
print(word[6:9]) # Prints 'sit'

word_2 = "definitely"
length = len(word_2)

# Print sliced strings
for n in range(length):
    print(n)
    print(word_2[:n+1])