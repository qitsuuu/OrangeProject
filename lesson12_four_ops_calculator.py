num1= input("Enter the first number: ")
if not num1.isalpha():
    num1=float(num1)
else:
    num1 = input("Enter the second number: ")

operation = input("Enter operation: ")
num2 = input("Enter the second number: ")
if not num2.isalpha():
    num2=float(num2)
else:
    num2 = input("Enter the second number: ")

#this calculator doesn't have loop yet
#therefore only until 2nd try for each input

if operation == "+":
    print("Value is: ", float(num1) + float(num2))
elif operation == "-":
    print("Value is: ", num1 - num2)
elif operation == "*":
    print("Value is: ", num1 * num2)
elif operation == "/":
    print("Value is: ", num1 / num2)
else:
    print("That is not a valid operation")
