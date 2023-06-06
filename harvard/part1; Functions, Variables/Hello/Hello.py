print("Hello world")

# Asking user for their name
name = input("What is your name? ")

# Remove whiepace from str
name = name.strip()

# Capitlize User's Name
name = name.title()

# You can also do this as well
'''name = input("What is your name? ").strip().title()'''

'''
# Spliet user's name into first name and last name
first, last = name.split(" ")
'''

# Says hello to user
print(f"Hello, {name} my good \"friend\"")
'''
The f is there so you can use just one set of "" instead of doing "wasd", wasd, "wasd". Instead you can just do "wasd {wasd} wasd"
'''