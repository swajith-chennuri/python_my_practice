a=int(input())
for i in range(65,65+a):
    for j in range(65, i+1):
        print(chr(j), end="")
    print()