name = input("What's your name? ")


with open("name.csv", "a") as file:
    file.write(f"{name}\n")

'''
or 
name = input("What's your name? ")


file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()
'''