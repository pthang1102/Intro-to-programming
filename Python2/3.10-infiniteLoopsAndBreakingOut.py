# This program keeps asking for new word and add it into an array until a word that is already in the array is entered.

def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me this word already!")
            break
        words.append(word)
    return words

no_repeating()