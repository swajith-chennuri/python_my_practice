n = int(input())
list1=list(map(int, input().split(' ')))
a=sorted(list1)
b=a[n-1]
c=[]
for x in a:
    if x!=b:
        c.append(x)
d=sorted(c)
print(d[-1])