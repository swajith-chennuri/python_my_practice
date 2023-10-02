weather=list(map(int,input().split(",")));c=",".join(str(i) for i in weather);print(c);b=c.split(",");print(b)
for i in range(0,len(b)):c=int(b[i]);print(c);print(type(c))