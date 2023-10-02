#check the given number is power of 2
a=int(input())
for i in range(0,a//4+2,1):
    if a==2**i:
        print("the given number is power of two")
        break
else:
    print("the given number is not a power of two")
    