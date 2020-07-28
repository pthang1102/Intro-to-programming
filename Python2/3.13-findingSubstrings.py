# This program counts the number of occurrences of a substring in a string.
def count_substring(string, substring):
    index = 0
    count = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            count += 1
        index += 1
    return count

print(count_substring('love, love, love, love, Love, all you need is love!', 'love')) # Should print 5