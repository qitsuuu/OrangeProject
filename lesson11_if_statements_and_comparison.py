num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
num3 = input("Enter the third number: ")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return  num1
    elif num2 >=num1 and num2 >= num3:
        return num2
    else:
        return num3

#print("Maximum number is " + str(max_num(num1, num2, num3)))

print("Maximum number is " + max_num(m1, num2, num3))