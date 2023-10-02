a=float(input("enter a = "))
b=float(input("enter b = "))
x=float(input("enter x = "))
f="sr university"
h="ananthasagar"
txt= "the best thing in life is to be single!"
t="helo world!"
print("a=",a)
print(type(a))
print("complex of a =",complex(a))
print("b=",b)
print(type(b))
print("complex of b =",complex(b))
c=a+b
print("addition of a and b = c =",c)
print(type(c))
d=b-a
print("subtraction of a from b = d =",d)
print(type(d))
e=a*b
print("multiplication of a and b = e =",e)
print(type(e))
print("f=",f)
print(type(f))
g=str(a)
print(type(g))
print(f,h)
print("x = ",x)
#given number is even or odd
print("a=",a)
print("b=",b)
if(a%2==0):
    print("the given number",a," is an even number")
else:
    print("the given number",a," is a odd number")
if(b%2==0):
    print("the given number",b,"is an even number")
else:
    print("the given number",b," is a odd number")
#given number is divisible or not
print("a=",a)
print("b=",b)
if(a%4==0 and a%6==0):
    print("the given number",a," is divisible by 4 and 6 ")
else:
    print("the given number",a," is not divisible by 4 and 6")
if(b%4==0 and b%6==0):
    print("the given number",b," is divisible by 4 and 6 ")
else:
    print("the given number",b," is not divisible by 4 and 6")
#grater of th numbers
print("a=",a)
print("b=",b)
print("x = ",x)
if(a>b and a>x):
    print("the given number",a," is grater than ",b,"and",x)
if(b>a and b>x):
    print("the given number",b," is grater than ",a,"and",x)
if(c>b and c>x):
    print("the given number",x," is grater than ",a,"and",b)
else:
    print("all three numbers are equal")
#assignment

print("x=",x)
x+=5
print("x+=5 ==",x)
x-=7
print("x-=7 ==",x)
x*=6
print("x*=6 ==",x)
x/=8
print("x/=8 ==",x)
x%=5
print("x%=5 ==",x)
x**=2
print("x**=2 ==",x)
x//=5
print("x//=5 ==",x)
#comparision operation
print("a=",a)
print("b=",b)
print("a=b",a==b)
print("a!=b",a!=b)
print("a>b",a>b)
print("a<b",a<b)
print("a>=b",a>=b)
print("a<=b",a<=b)
#if a in b or a not in b
print("a is b",a is b)
print("a is not b",a is not b)
print("h in f",h in f)
print("h not in f",h not in f)
#to print text
print(txt)
print("single!"in txt)
print("single!"not in txt)
print(t)
print("t[2:8]=",t[2:8])
print("t[:8]=",t[:8])
print("t[2:]=",t[2:])
print("t[0:]=",t[0:])
print("t[:]=",t[:])
print("t[-4:-2]=",t[-4:-2])
print("t[-6:-4]=",t[-6:-4])
print("length of t",len(t))
print(t.upper())
print("replacing hello with python in string t",t.replace("hello","python"))
print(t)
print(t[1:4].upper())