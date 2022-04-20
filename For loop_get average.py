grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade      ##The 'total += grade' is the same as typing 'total = total + grade'

print(total / amount)



grades = [35, 67, 98, 100, 100]
total = sum(grades)            ##This method uses the 'sum' function to automatically add up the total of the entire list 'grades'.
amount = len(grades)

print(total / amount)
