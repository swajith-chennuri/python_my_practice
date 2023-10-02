def varsha(a,b):
    c=a*b
    return c
l=[]
n=int(input("enter the length of list you want = "))
for i in range(0,n):
    a=int(input())
    l.append(a)
print(l)
for i in range (0,len(l)-1):
    d=varsha(l[i],l[i+1])
    print(d)