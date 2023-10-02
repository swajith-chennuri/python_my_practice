a=int(input("enter the value of a = "))
b=int(input("enter the value of b = "))
c=int(input("enter the value of c = "))
#nested conditions
if(a>b):
    if(a>c):
        print(a," is greater than" ,b ,"and", c)
elif(b>c)and(b>a):
    print(b, "is greater than", a ,"and", c)
else:
    print(c, "is greater than", a ,"and", b)