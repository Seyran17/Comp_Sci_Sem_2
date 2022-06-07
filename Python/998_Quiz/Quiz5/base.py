num = input("Please say your favorite number in a full sentance ")
age = int(input("what is your age "))
for i in range(len(num)):
    if num[i]=="1" or num[i]=="2" or num[i]=="3" or num[i]=="4" or num[i]=="5" or num[i]=="6" or num[i]=="7" or num[i]=="8" or num[i]=="9" or num[i]=="0":
        num = num[i:len(num)] 
        break
print(" ")
print("Your favorite number multiplied by your age is")
print(int(num)*age)
