bike=input("enter the bike you want = ")
a=["heavyduty","cheethak","passion","rx100","duke","re"]
if(bike in a):
    if(bike=="heavyduty"):
        print("50cc and 100cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==50)or(cc==100):
            print("green and blue are available")
        else:
            print("the given cc is not available")
    elif(bike=="cheethak"):
        print("100cc,120cc and 110cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==100)or(cc==120)or(cc==110):
            print("silver and black are available")
        else:
            print("the given cc is not available")
    elif(bike=="passion"):
        print("120cc and 150cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==120)or(cc==150):
            print("blue,yellow and red are available")
        else:
            print("the given cc is not available")
    elif(bike=="rx100"):
        print("only 100cc available")
        cc=int(input("enter the cc you want = "))
        if (cc==100):
            print("blue,black and red are available")
        else:
            print("the given cc is not available")
    elif(bike=="duke"):
        print("125cc,290cc and 390cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==125)or (cc==290) or (cc==390) :
            print("silver and black are available")
        else:
            print("the given cc is not available")
    elif(bike=="re"):
        print("350cc,500cc/fuel type desile and 650cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==350)or (cc==650):
            print("crome and black are available")
        elif (cc==500):
            print("crome and black desile bike are available")
        else:
            print("the given cc is not available")
else :
    print("the bike is not available in our showroom")
