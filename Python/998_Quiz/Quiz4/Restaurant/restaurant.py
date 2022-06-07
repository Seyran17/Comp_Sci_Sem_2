import random

restaurants = ["mcdonalds", "wendys", "tacobell"]
mcdonalds = ["bigmac", "mcnuggets", "frenchfries"]
wendys = ["steak", "wendy", "sauce"]
tacobell = ["taco", "shakes", "bell"]

restaurantinput = input("What restaurant do u want to order from. your options are mcdonalds, tacobell, and wendys")

if restaurantinput == "mcdonalds":
    print("The menu for this restaurant is " + mcdonalds)
    item = mcdonalds[random.randrange(0,3)]
    print("the suggested item is " + item)
    
if restaurantinput == "wendys":
    print("The menu for this restaurant is " + wendys)
    witem = wendys[random.randrange(0,3)]
    print("the suggested item is " + witem)
    
if restaurantinput == "tacobell":
    print("The menu for this restaurant is " + tacobell)
    titem = tacobell[random.randrange(0,3)]
    print("the suggested item is " + titem)