a=[2,7,7,9,2,9,7,2,8,6,6,9]
for i in range (0,len(a),1):
    c=0
    for j in range (0,len(a),1):
        if (a[i]==a[j]):
            c=c+1
    print(a[i],"is repeated",c,"times")
            