t1 = ()
t2 = (1,2,3,4,5)
print("t1 = ",t1)
print("t2 = ",t2)
for i in range (1,11):
    t1 += (i,)
print("now t1 = ",t1)
print("maximum  in  t1 = ",max(t1))
print("minimum  in  t1 = ",min(t1))
print("sum of elements  in  t1 = ",sum(t1))