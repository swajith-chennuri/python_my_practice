bike=input("enter the bike you want = ")
a=["heavyduty","chectak","passion","rx100","duke","re"]
if(bike in a):
    if(bike=="heavyduty"):
        print("50cc and 100cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==50):
            print("green and blue colors are available")
        elif (cc==100):
            print("gray color is  available")
        else:
            print("the given cc is not available")
    elif(bike=="chectak"):
        print("100cc,120cc and 110cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==100):
            print("red and blue colors are available")
        elif (cc==120):
            print("silver color is  available")
        else:
            print("the given cc is not available")
    elif(bike=="passion"):
        print("110cc and 200cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==110):
            print("pink and yellow are available")
        elif (cc==200):
            print("green is available")
        else:
            print("the given cc is not available")
    elif(bike=="rx100"):
        print("125cc and 220cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==125):
            print("blue and green colors are available")
        elif (cc==220):
            print("blue color is available")
        else:
            print("the given cc is not available")
    elif(bike=="duke"):
        print("125cc,290cc and 390cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==125):
            print("blue0 color is available")
        elif (cc==290):
            print("black color is  available")
        elif (cc==390):
            print("silver and black are available")
        else:
            print("the given cc is not available")
    elif(bike=="re"):
        print("350cc,500cc/fuel type desile and 650cc are available")
        cc=int(input("enter the cc you want = "))
        if (cc==350):
            print("red color is available")
        elif (cc==500):
            print("chrome and black desile bike are available")
        elif (cc==650):
            print("chrome color is  available")
        else:
            print("the given cc is not available")
else :
    print("the bike is not available in our showroom")
