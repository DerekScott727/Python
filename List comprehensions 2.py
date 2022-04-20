friends = ["Rolf", "Sam", "John", "Steve", "Sawyer"]
starts_s = []

for friend in friends:           ##for loop to state what list/variables will be affected (for the friend element in friends, do the following)
    if friend.startswith("S"):    ##if statement to detail the condition with the '.startswith' function (if friend starts with "S", then do the following)
        starts_s.append(friend)     ##use the .append to complete the process, to add whatever element in 'friends' list, to the starts_s list.

print(starts_s)

