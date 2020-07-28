# This program finds and replace all instances of an undesirable substring by a given replacement.
def replace_substring(string, sub, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(sub)] == sub:
            index += len(sub)
            output.append(replacement)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

print(replace_substring('Scrambled SPAM!s, bacon, and toast.', 'SPAM!', 'egg'))
