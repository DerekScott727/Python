name = 'Bob'
greeting = f'Hello, {name}.'    ### Embeds the variable 'name' in the variable 'greeting'. f-string does NOT change dynamically

print(greeting)

name = 'Rolf'

print(greeting)    ###Because the f-string doesnt change dynamically, greeting wont update the 'name' variable to the new name of Rolf.
                   ### You will need to use the f-string again, to capture the latest value of the 'name' variable


greeting = f'Hello, {name}.'
print(greeting)
