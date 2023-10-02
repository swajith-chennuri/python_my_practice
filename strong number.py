a=int(input("enter the number = "))
count=0
k=a
while(a!=0):
    temp=a%10
    a=a//10
    b=1
    for i in range (1,temp+1,1):
        b=b*i
    count=count+b
if(k==count):
    print("the given number is strong")
else:
    print("the given number is not strong")