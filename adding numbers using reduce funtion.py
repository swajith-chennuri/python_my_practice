from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)