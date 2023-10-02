a=int(input())
b=int(input())
t=a>>b
print(t)
if t%2==0:
    print("that is not a set bit")
else:
    print("that is a set bit")