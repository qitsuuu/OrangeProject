print("Here's exponent value checker program!\n")
def raise_to_power():
    basenum = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    result= 1
    for index in range(exponent):
        result = result * basenum #store the current math while basenum remains unchanged
    print(f"{result}\n")

    print("Do you want to try again? y/n")
    if input() == "y":
        raise_to_power()

raise_to_power()