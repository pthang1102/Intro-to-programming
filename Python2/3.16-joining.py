# This function tests built-in function 'join'. It adds '<br>' between each 2 lines.
def breakify(strings):
    return '<br>'.join(strings)

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

print(breakify(lines))