phrase="Welcome to Japan"
occurence = 2

print(phrase)
print("uppercase: " + phrase.upper() + " " +str(occurence))
print("lowercase: " + phrase.lower())
print("boolean: " + str(phrase.upper().isupper()))
print("length: " + str(len(phrase)))
print("capitalize: "+ phrase.capitalize() + "\n")
print(phrase[9])
print(phrase.index("o"))
print(phrase.replace("Japan","Europe"))

ind = [i for i, val in enumerate(phrase) if val == "o"]
print(ind)