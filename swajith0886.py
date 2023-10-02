t1 = ()
t2 = (1,2,3,4,5)
print("t1 = ",t1)
print("t2 = ",t2)
for i in range (1,11):
    t1 += (i,)
print("now t1 = ",t1)
print("t1[2:5] = ",t1[2:5])
print("t1[:] = ",t1[:])
print("length of t1 = ",len(t1))
t3 = t1+t2
print("t3 = ",t3)
print("repeataion of t2 ",t2*3)