#This is a basic function
def say_hi(name, age):
    print("Hey " + name)
    print("Congratulations for turning to chapter " + str(age))

say_hi("Qit", 27)

#This is a function with return statement
def cube(num):
    return num*num*num

result = str(cube(3))
print("cube: " +result)
