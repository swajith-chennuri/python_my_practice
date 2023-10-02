#with recursion function
def exp(a,b):
    if b==0:
        return 1
    else :
        return a*exp(a,b-1)
def exp1(a,b):
    return (a**b)
a=int(input("enter the number"))
b=int(input("enter the number"))
print(exp(a,b))
print(exp1(a,b))

