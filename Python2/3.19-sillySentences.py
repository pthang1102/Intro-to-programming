# This program generates silly sentences from templates, nouns and verbs 
# which are RANDOMLY picked from words.py module.

import random
import words

def silly_strings(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We will append strings into this list for output.
    output = []
    
    # Keep track of where in the template string we are.
    index = 0

    while index < len(template):
        if template[index:index+len('{{noun}}')] == '{{noun}}':
            # Add a random noun to the output.
            output.append(random.choice(nouns))
            index += len('{{noun}}')
        elif template[index:index+len('{{verb}}')] == '{{verb}}':
            # Add a random verb to the output.
            output.append(random.choice(verbs))
            index += len('{{verb}}')
        else:
            # Copy a character to the output.
            output.append(template[index])
            index += 1
    
    return "".join(output)

print(silly_strings(words.nouns, words.verbs, words.templates))
print(silly_strings(words.nouns, words.verbs, words.templates))
print(silly_strings(words.nouns, words.verbs, words.templates))
