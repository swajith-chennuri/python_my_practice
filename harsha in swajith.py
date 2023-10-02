a=input("enter the word")
b=input("enter the 2nd word")
c=sorted(a)
d=sorted(b)
for i in range(0,len(d),1):
    e=d[i]
    if e in c:
        print("yes")
    else:
        print("no")
    

