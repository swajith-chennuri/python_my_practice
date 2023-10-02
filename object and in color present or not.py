ob=input("enter the object you want = ")
color=input("enter the color you want = ")
if (ob=="bowl"or ob=="cup"or ob=="plate")and (color=="green" or color=="blue" or color=="black"):
    print(ob,"in colour of ",color,"is present")
elif(ob=="pot")and(color=="blue" or color=="black"):
    print(ob,"in colour of ",color,"is present")
else:
    print(ob,"in colour of ",color,"is not present")