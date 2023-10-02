import sys
number = input("enter mobile number")
if(len(number) != 10 or (number[0]==0 or number[0]==1 or number[0]==2)):
   print("Invalid Number")
   sys.exit(0)
for char in number:
    if(char.isalpha()):
        print("valid Number")
        break
else:
    print("invalid number")
