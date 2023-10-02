#creating empty dictionary
dictionary = dict()
print(dictionary)
dic = {}
print("empty dictionary = ",dic)
#creation of dictionary with three values
dic1 = {'HTNO':'2205A41L03','Name':'swajith','course':'ECE b.tech'}
print("dictionary dic1 = ",dic1)
#creating dictionary usin dict() function
dic2 = dict([('HTNO','2205A41L03'),('Name','swajith'),('course','ECE b.tech')])
print("dictionary dic2 = ",dic2)
#creating dictionary with 10key
dic3 = { x : 2*x for x in range(1,11)}
print("dictionary dic3 = ",dic3)
dic4 = { x : 5*x for x in range(1,11)}
print("dictionary dic4 = ",dic4)