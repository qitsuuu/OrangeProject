num1= input("Enter the first number: ")
if num1.isalpha():
    num1 = input("Enter the second number: ")
    #if will not use float(), arithmetic ops will not work on str
num1=float(num1)

operation = input("Enter operation: ")
num2 = input("Enter the second number: ")
if num2.isalpha():
    num2 = input("Enter the second number: ")
num2=float(num2)

#this calculator doesn't have loop yet
#therefore only until 2nd try for each input

if operation == "+":
    print("Value is: ", num1 + num2)
elif operation == "-":
    print("Value is: ", num1 - num2)
elif operation == "*":
    print("Value is: ", num1 * num2)
elif operation == "/":
    print("Value is: ", num1 / num2)
else:
    print("That is not a valid operation")
