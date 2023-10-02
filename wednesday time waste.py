a=input("enter the day = ")
b=60
c=15
d=15
if a=="wed":
    print("morning",b ,"min")
    print("break",c ,"min")
    print("break",d ,"min")
    print("total",b+c+d,"min")
elif a=="mon" or a=="tue" or a=="thu"or a=="fri"or a=="sat" or a=="sun":
    print("time not wasted")
else:
    print("day not found")