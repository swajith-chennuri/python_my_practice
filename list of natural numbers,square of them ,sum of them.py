def filter(a):
    d=[];b=[]
    for i in range(1,a+1):
        b.append(i**2)
        d.append(i)
    print(d);print(b);c=sum(b);print(c)
    return
a=int(input());filter(a)