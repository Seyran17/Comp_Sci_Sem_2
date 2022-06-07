b = int(input("Please enter your line length "))
a = input("Do you want a horizontal or vertical line ")
if a == "horizontal":
    for x in range(0,b):
        print("*", end="")
if a == "vertical":
    for x in range(0,b):
        print("*")
 