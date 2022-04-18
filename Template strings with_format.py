name = "Bob"
greeting = 'Hello, {}.'                    ###The curly bracers here are essentially a function called 'format'
with_name = greeting.format(name)         ### The .format is calling the format function inside of 'greeting' and telling the template to use 'name'

with_name_two = greeting.format("Rolf")  ### This time we tell the format function to not use 'name' but to use this new input we manually typed "Rolf"

print(with_name)
print(with_name_two)
