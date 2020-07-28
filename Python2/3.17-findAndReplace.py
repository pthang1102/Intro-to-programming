# This program finds and removes all instances of an undesirable substring from a given string.
def remove_substring(string, sub):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(sub)] == sub:
            index += len(sub)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
print(remove_substring('Whoever<br> wrote <br>this<br> loves<br> break tags<br>', '<br>'))
print(remove_substring('I amNOT learning to code', 'NOT'))
