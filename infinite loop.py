number = 7


while True:      ##When using the True keyword to make an infinite loop, you will need to create a way to end the loop from within the loop itself (Using the break keyword below)

    user_input = input("Would like to play? (Y/n) ")

    if user_input =='n':
        break                                         ##The break keyword will end the loop.

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    else:
        print("Sorry, that is the wrong number.")

    user_input = input("Would like to play again? (Y/n) ")
    if user_input == 'n':
        print("Game is over.")
        break
