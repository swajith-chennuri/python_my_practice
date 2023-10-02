a=int(input("enter the number = "))
count=0
k=a
while(a!=0):
    temp=a%10
    a=a//10
    count=count+(temp**3)
if(k==count):
    print("the given number is amstrong")
else:
    print("the given number is not amstrong")