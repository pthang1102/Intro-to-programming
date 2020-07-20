# Loop over a string and count how many letter 'a' there are
count = 0

for ch in "What an amazing day today. I practiced coding and played my favorite game!":
    if ch == "a":
        count += 1

print('There are', count, 'letter "a" in this string.')