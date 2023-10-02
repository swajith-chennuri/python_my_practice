#method 1
a=input("enter the animal name = ")
if a=="tiger":
    print("tiger does exist")
elif a=="lion":
    print("lion does exist")
elif a=="bear":
    print("bear does exist")
else:
    print("the animal does not exist")
# method 2
c=input("enter the animal name = ")
if c=="tiger" or c=="bear" or c=="lion":
    print(c,"is exist")
else:
     print("the animal does not exist")
#method 3
b=["lion","tiger","bear"]
e=input("enter the animal name = ")
if e in b :
    print("the animal is exist")
else :
    print("the animal not exist")