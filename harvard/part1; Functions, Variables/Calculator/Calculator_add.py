
x = float(input("What is x? "))
y = float(input("What is y? "))

z= round(x+y) # The number will be rouned to the nearest whole number



print(f"≈{z:,}") # The {z:,} lets python know that when you have a number like 10000 that it will put like 10,000 . You can also change the , to a . or whatever you want it to be

# These ones have int for whole numbers but float lets you use decimcals
# Or you can also do this
'''
x = input("What is x? ")
y = input("What is y?")

z = int(x) + int(y)

print(z)
'''
# OR (Not suggested at all but possable)
'''
print(int(input("What is x? ")) + int(input("What is y? ")))
'''
