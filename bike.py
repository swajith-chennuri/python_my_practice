a=["heavyduty","chectak","passion","rx100","duke","royal enfield"]
bike=input("enter the bike you want = ")
cc=int(input("enter the cc you want = "))
color=input("enter the color you want")
if(bike in a):
    if(bike=="heavyduty"):
        if (cc==50):
            if(color=="green" or color=="blue"):
                print("the bike is present")
            else:
                print("the bike color is not present")
                
        elif (cc==100):
            if (color=="green" or color=="blue"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")
    if(bike=="cheethak"):
        if (cc==100):
            if(color=="siver" or color=="gray"or color=="black"):
                print("the bike is present")
            else:
                print("the bike color is not present")
                
        elif (cc==120):
            if (color=="siver" or color=="gray"or color=="black"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")
    if(bike=="passion"):
        if (cc==120):
            if(color=="yellow" or color=="blue" or color=="blue"):
                print("the bike is present")
            else:
                print("the bike color is not present")
                
        elif (cc==150):
            if (color=="yellow" or color=="blue" or color=="blue"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")
    if(bike=="rx100"):
        if (cc==150):
            if(color=="red" or color=="blue" or color=="black"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")
    if(bike=="duke"):
        if (cc==125):
            if(color=="orange" or color=="white"):
                print("the bike is present")
            else:
                print("the bike color is not present")
                
        elif (cc==290):
            if (color=="orange" or color=="white"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        elif (cc==390):
            if (color=="orange" or color=="white"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")
    if(bike=="royal enfield"):
        if (cc==350):
            if(color=="black" or color=="crome"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        if (cc==500):
            print("the bike is desile fuel")
            if(color=="black" or color=="crome"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        if (cc==650):
            if(color=="black" or color=="crome"):
                print("the bike is present")
            else:
                print("the bike color is not present")
        else:
            print("the given cc is not present")

else :
    print("the bike is not present in our showroom")