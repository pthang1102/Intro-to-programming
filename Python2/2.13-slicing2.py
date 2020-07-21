# Create a function to print the given word in a triangular pattern
def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])

word_triangle("ABRACADABRA")
