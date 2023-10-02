import re
txt = "the rain in spain"
x= re.search("ai",txt)
print(x)#this will print an object
txt = "the rain in spain"
x= re.search(r"\bs\w+",txt)
print(x.span())
txt = "the rain in spain"
x= re.search(r"\bs\w+",txt)
print(x.group())
