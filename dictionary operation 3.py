print("example of delete / remove items in dictionaries")
#two dictionaries with  three values
dic1 = {'HTNO':'2205A41L03','Name':'swajith','course':'ECE b.tech'}
dic2 = {'HTNO':'2205A41L04','Name':'h@rsha','course':'ECE b.tech'}
print("dictionary1",dic1)
print("After sorting keys in sorted order dictionry1 = ",sorted(dic1.key))
del('Name')
print("after deletiing course entry in dictionar1 = ",dic1)
dic1.pop('Name')
print("after pop method removing name entry in dictionary1 = ",dic1)