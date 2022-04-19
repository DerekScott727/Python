friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)    ##The ".difference" function calculates the difference between the first set and the set in parenthesis.
                                              ## Meaning, it will output whatever is stored in the first set that is not in the second set.
print(local_friends)


local = {"Rolf"}
friends = local.union(abroad)                ## The ".union" function combines two sets.
print(friends)
