friends = ["jon", "james", "joanna", "tom"]
starts_j = [friend for friend in friends if friend.startswith("j")]

for friend in friends:
    if friend.startswith("j"):
     starts_j.append(friend)

print(starts_j)
