#make a list called numbers and make a second list called doubled which has the elements from the numbers list doubled

numbers = [2, 3, 6]
doubled = [x * 2 for x in numbers]     ##x * 2 creates varibable 'x' an multiplies it by 2, then 'for x in numbers' it says the elements in numbers should loop the previous command.

print(doubled)
