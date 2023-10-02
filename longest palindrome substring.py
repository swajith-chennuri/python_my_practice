def a(s):
    n = len(s)
    c = ""  
    for i in range(n):
        for j in range(i, n):
            d = s[i:j+1]
            if d == d[::-1] and len(d) > len(c):
                c = d 
    return c
b = input()
result = a(b)
print(result)