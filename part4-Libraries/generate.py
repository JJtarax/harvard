import random #Docs.python.org/3/libary/random.html
#Coin filp
coin = random.choice(["Heads" , "Tails"])
print(coin)
#random number from 1-10
number = random.randint(1,10)
print(number)
#random order of jack, queen, king
cards = ["jack" , "queen" , "king"]
random.shuffle(cards)
for card in cards:
    print(card)
