def divide(x,y):
    return x/y
def calc(x,y):
    return (x*divide(x,y))
try:
    
    #print(calc("Hello",1))
    print(divide(5,0))
except TypeError:
    print("type mis matched")
except ZeroDivisionError:
    print("Zero Division Error")
except Exception: 
    print("Execption occured")

