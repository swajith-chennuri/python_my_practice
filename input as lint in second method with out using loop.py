a=list(map(int,input().split(",")))
for i in range (0,len(a),1):
    c=0
    for j in range (0,len(a),1):
        if (a[i]==a[j]):
            c=c+1
    if (c==1):
        print(a[i],"is odd number")