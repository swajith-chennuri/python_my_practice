distance=10
distance1 , distance2 , distance3 = 10, 25, 20
s1 = "the distance from hanumkonda to SR university is {}"
print(s1.format(distance))
s2="""the distance from hanumkonda to SR university is {2}
the distance from warangal to SR university is {0},
the distance from kazipet to SR university is {1}"""
print(s2.format(distance1,distance2,distance3))