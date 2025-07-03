secretword = ("orange", "pie", "blue", "mochi")
guessword = input("Enter your guess: ")
#while guessword != secretword:
#    guessword = input("Enter your guess: ")
x=0


for x in secretword:
    print(x)
    while guessword != x:
        print("\nYou guessed the incorrect")

guessword = input("Enter your guess: ")
