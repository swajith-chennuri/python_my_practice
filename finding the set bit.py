#convert a decimal number to binary
a=int(input())
b=int(input())
print(bin(a))
k=bin(a)
if b<len(k):
   d=k[2:]
   c=d[b]
   print("bit at index of ",b,"is",c)
   if c=="1":
        print("the setbit is 1")
   if c=="0":
        print("the setbit is 0")
else :
    print(b,"is out of range")
