l=list(map(str,input().split(",")))
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
word_count = {}
for word in d:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += d[word] 
    else:
        word_count[word_lower] = d[word]  
for word in word_count:
    print(word + "=" + str(word_count[word]))
