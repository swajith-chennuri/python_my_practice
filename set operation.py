s = {1,2.0,'abc'}
print("the set = ",s)
print("1. converting list into set")
list1 = [5,4,5,3,1,2,2]
s1 = set(list1)
print("list is converted into set = ",s1)
print("2. converting Tuple into set")
Tuple1 = (6,7,8,9,10)
s2 = set(Tuple1)
print("2. Tuple is converted into set = ",s2)
print("3. converting string characters into set")
s3 = set("SR University")
print("string characters is converted into set = ",s3)
print("4. converting string words into set = ")
str1 = "SR University Warangal"
s4 = set(str1.split())
print("string words is converted into set = ",s4)
s5 = set()
print("set5 = ",s5)
for i in range(1,11):
    s5.add(i)
print("now set5 = ",s5)
