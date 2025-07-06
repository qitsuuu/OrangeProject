def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "q"
        else:
            translation =translation + letter
    print(translation)

    print("\nDo you want to try again? y/n ")
    if input() == "y":
        translate(input("Enter a phrase: "))

translate(input("Enter a phrase: "))