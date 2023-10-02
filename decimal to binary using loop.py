#convert a decimal number to binary
a=int(input())
c=[]
while(a!=0):
    b=a%2
    a=int(a/2)
    c.append(b)
d=c[::-1]
print(d)
b=int(input("enter the "))
if b<len(d):
   c=d[b]
   print("bit at index of ",b,"is",c)
    if c=="1":
        print("the setbit is 1")
    if c=="0":
        print("the setbit is 0")
else :
    print(b,"is out of range")