number = 7
user_input = input("Would like to play? (Y/n) ") ##The (Y/n) is a common convention, if user types anything other then 'n', 'Y' will be the default
                                                      ##They will have to specifically type 'n' if they want to stop



while user_input != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    else:
        print("Sorry, that is the wrong number.")

    user_input = input("Would like to play again? (Y/n) ")
    if user_input == 'n':
        print("Game is over.")
