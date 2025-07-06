def secretwordgame():
    secretwords = ("orange", "pie", "blueberry", "mochi")
    #secret_word = random.choice(secret_words) can use if need to guess a specific word
    max_attempts = 3
    attempts = 0

    #simple and short method
    #while guessword not in secretword:
    #    guessword = input("Enter your guess: ")

    print("""Welcome to the Guessing Game!
I'm thinking of foods that starts with 'o', 'p', 'b' and 'm'.
Can you guess any of them?\n""")

    while attempts < max_attempts:
    #for attempt in range(max_attempts): for loop version
        attempts +=1
        guessword = input(f"Attempt {attempts}: Enter your guess: ")

        if guessword in secretwords:
            print(f"You guessed the word '{guessword}' in {attempts} attempts.\n")
            break

        elif attempts == max_attempts:
            print("You've ran out of attempts. Thank you for playing!\n")
        else:
            print("Nice guess. Try again!\n")

    retry = input("Would you like to try again? y/n? \n")

    if retry == "y":
        secretwordgame()

secretwordgame()

