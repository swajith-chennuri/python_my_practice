# write a single line program to combine print elements of two list using list comprehension
#list1=[10, 20, 30]
#list2=[30, 10, 40]
#output:
print([(a, b) for a in [10, 20, 30] for b in [30, 10, 40] if a != b])