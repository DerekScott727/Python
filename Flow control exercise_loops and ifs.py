# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [2, 4, 6, 8]
for number in numbers:
    if number % 2 == 0:          ##'if number is divisible by 2'
    evens.append(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == 'q':     ##Elif will be quicker then another if statement. You can use elif because the user will never be able to input both 'a' and 'q'
    print("Quit")
