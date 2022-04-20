day_of_week = input("What day of the week is it today? ").lower()          ##The .lower() function turns user's entire input into lowercase

if day_of_week == "monday":             ###After using the .lower() function for the input, now we ensure the if statement knows to accept lowercase as well.
    print("Today is Monday.")
elif day_of_week == "tuesday":
    print("Today is Tuesday.")
else:
    print("The week is almost over!")
