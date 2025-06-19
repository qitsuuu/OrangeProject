#trying to contsruct own function with if conditions
is_female= input("Are you a female ?")
if is_female == "yes" or is_female == "True":
    is_female=True
else:
    is_female=False
is_tall = input("Are you tall ?")
if is_tall == "yes" or is_tall == "True":
    is_tall=True
else:
    is_tall=False

def person(is_female, is_tall):
    if is_female and is_tall:
        print("You are a tall female.")
    elif is_female and not is_tall:
        print("You are a female but NOT tall.")
    elif not is_female and is_tall:
        print("You are NOT a  female but are tall.")
    else:
        print("You are NOT a  female and NOT tall.")


person(is_female, is_tall)