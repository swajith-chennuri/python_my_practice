#dictionary with three values
dic1 = {'HTNO':'2205A41L03','Name':'swajith','course':'ECE b.tech'}
dic2 = {'HTNO':'2205A41L04','Name':'h@rsha','course':'ECE b.tech'}
print("dictionary1",dic1)
print("dictionary2",dic2)
print("HTNO in dic1",dic1['HTNO'])
print("Name in dic1",dic1['Name'])
print("course in dic2",dic2['course'])
#adding new entries in dic1,dic2
dic1['Year'] = dic2['Year'] = '1st year'
dic1['sem'] = dic2['sem'] = '2nd sem'
dic2['special']= 'electronic'
dic1.update(dic2)
print("after updation dictionary1 = ",dic1)
print("after updation dictionary2 = ",dic2)
#modifying course entry in dic2
dic2['cource'] = 'CSE b.tech'
print("after modifying dictionary2 = ",dic2)
#looping in dictionary
print("looping in dictionary1")
print("key   : ",end = " ")
for key in dic1:
    print(key, end = ' | ')#accessing only key
print("\nValues : ",end = " ")
for value in dic1.values():
    print(value,end = " | ")#accessing the values
#accessing key and values in dictionary
    