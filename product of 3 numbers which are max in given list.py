def b(a):
    if len(a)<3:
        return 0
    else:
        c=max(a)
        a.remove(c)
        d=max(a)
        a.remove(d)
        e=max(a)
        print(c*d*e)
    return
a=list(map(int,input().split(",")))
b(a)
