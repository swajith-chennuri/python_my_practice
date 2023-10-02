import random
b,c,g,h=0,0,0,0;d=6;e=6;a=[];j=[];
while(c+b!=d+e):
    if b<d or c<e:
       f=input()
    if b<d and f=="s":
        b=b+1
        dice_roll = random.randint(1,6)
        print("You rolled a", dice_roll)
        a.append(dice_roll)
        g=dice_roll+g
        if dice_roll==6:
            d=d+1
    if c<e and f=="f":
        c=c+1
        dice_roll = random.randint(1,6)
        print("You rolled a", dice_roll)
        j.append(dice_roll)
        if dice_roll==6:
            e=e+1
        h=dice_roll+h
print("player1 rolls",a)
print("player1 score",g)
print("player2 rolls",j)
print("player2 score",h)
if g>h:
    print("player 1 win")
elif h>g:
    print("player 2 win")
else:
    print("match draw")