def square(i):
    return i ** 2
squares = list(filter(square, range(1, 11)))
even_squares = list(filter(lambda x: x % 2 == 0, squares))
for i in range(0,len(squares)):
    if squares[i]% 2 == 0 and squares[i] % 4 == 0:
        print(squares[i],end=" ")
print()
print("list of even squares in range 1-10:", even_squares)
