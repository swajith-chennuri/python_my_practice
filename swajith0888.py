t1 = ()
t2 = (1,2,3,4,5)
print("t1 = ",t1)
print("t2 = ",t2)
for i in range (1,11):
    t1 += (i,)
print("now t1 = ",t1)
for i in t1:
    print(i,end = "  ")