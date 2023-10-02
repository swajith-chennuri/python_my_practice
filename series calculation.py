#1/1^2+1/2^2+.......1/n^2
a=int(input())
c=0
for i in range (1,a+1,1):
    c=c+1/i**2
print(c)