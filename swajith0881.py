#pythyon list
l1 = [1,2,3,4,5,]
l2 = [6,7,8,9,10]
print("l1[0:2] = ",l1[0:2])
print("l1[:] = ",l1[:])
l1[2] =10
print("l1 = ",l1)
l3=[]
for i in range(1,21):
    l3.append(i)
print("13 = ",l3)
del(l3[5])
print("13 = ",l3)
del(l2)
print("12 = ",l2)