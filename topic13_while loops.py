num = int(input("Enter a number: "))
def testing(count):
    i=1
    while i<=count:
        if i%2!=0:
            print("I am ODD number ", i)
        elif i % 2 == 0:
            print("I am EVEN number ", i)
        i +=1
    print("\nOut of the Loop")

testing(num)

