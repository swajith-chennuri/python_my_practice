#task-1
#level-1 user has to ans the all three questions .shoud attempt all three questions atleast one should correct
#level-2 user has to correct ans two questions out of the three questions
#level-3 user hat to correct two out of  the three questions
print("level-1")
a=0
print("complete the series A B _")
print("a,A  b,B  c,C  d,D")
b=input()
if(b=="c"):
    a=a+1000
    print("correct ans you won",1000)
if(b!="c"):
    print("ans is wrong")
print("complete the series 1 2 _")
print("a,1  b,2  c,3  d,4")
c=input()
if(c=="c"):
    a=a+1000
    print("correct ans you won",a)
if(c!="c"):
    print("ans is wrong")
print("complete the series 3+2 _")
print("a,4  b,5  c,25  d,10")
e=input()
if(e=="b"):
    a=a+1000
    print("correct ans you won",a)
if(e!="b"):
    print("ans is wrong")
if a==0:
    print("you lost 1st level")
if a>=1000:
    print("level-2")
    print("complete the series d h _")
    print("a,a b,f  c,l  d,e")
    b=input()
    if(b=="c"):
         a=a+10000
         print("correct ans you won",a)
    if(b!="c"):
        print("ans is wrong")
    print("complete the series 10 20 _")
    print("a,29  b,30  c,10  d,40")
    c=input()
    if(c=="b"):
        a=a+10000
        print("correct ans you won",a)
    if(c!="b"):
        print("ans is wrong")
    print("complete the series 30+80 _")
    print("a,10  b,100  c,50  d,120")
    e=input()
    if e=="b":
        a=a+10000
        print("correct ans you won",a)
    if(b!="c"):
        print("ans is wrong")
    if a<20000:
        print("you lost 1st level")
    if a>=20000:
        print("level-3")
        print("complete the series e h _")
        print("a,a b,f  c,l  d,e")
        b=input()
        if(b=="c"):
             a=a+100000
             print("correct ans you won",a)
        if(b!="c"):
             print("ans is wrong")
        print("complete the series 10 20 _")
        print("a,29  b,30  c,10  d,40")
        c=input()
        if(c=="b"):
            a=a+100000
            print("correct ans you won",a)
        if(b!="c")and(c!="b"):
            print("you lost the level 3")
        if(b=="c")and(c!="b") :
            print("ans is wrong")
        if ((b=="c")and(c!="b")) or ((b!="c")and(c=="b"))or((b=="c")and(c=="b")):
            print("complete the series 40 80 _")
            print("a,10  b,120  c,50  d,110")
            e=input()
            if e=="b":
                a=a+100000
                print("correct ans you won",a)
            if e!="b":
                print("ans is wrong")
            if a<221000:
                print("you lost level 3")
if a>=221000:
    print("you lost the game")