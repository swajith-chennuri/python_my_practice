list1 = [1,2,5,3,4]
list2 = [8,7,6,3,5,4]
set1 = set(list1)
set2 = set(list2)
print("the set1 = ",set1)
print("the set2 = ",set2)
print("1. intersection of two sets")
print("intersection elements in both sets = ",set1.intersection(set2))
print("2.union of two sets")
print("union elements in both sets = ",set.union(set2))
print("3.difference in both sets")
print("elements which are in set1 ,not in set2 = ",set1.difference(set2))
print("elements which are in set2 ,not in set1 = ",set2.difference(set1))
print("4. elements which are belongs any one of set, not belongs to the intersection elements = ",set1.symmetric_difference(set2))