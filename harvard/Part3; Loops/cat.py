#While loop
i = 3
while i != 0:
    print("meow")
    i -= 1

#For loop
for _ in range(3): #The _ is there as somthing that you can use as a "varable" for when you need it but don't want to place a real one (aka place holder)
    print("meow")

#A way to do it in the print function
print("meow\n" * 3, end="")

#A way that has the user put in the amout of meow
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")


main()