try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(f"You can't divide by zero.\n{err}")
except ValueError as err:
    print(f"That was an Invalid input.\n{err}")