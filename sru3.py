a=["mamith","suhas","kalik","sreja","rishitha","varsha"]
mamith = {'gender':'male','branch':'cse','rollnumber':'1','age':'20','g.p.a':'9.8','speciality':'developer'}
suhas = {'gender':'male','branch':'cse','rollnumber':'2','age':'60','g.p.a':'9.8',"speciality":"art"}
kalik = {'gender':'male','branch':'cse','rollnumber':'3','age':'19','g.p.a':'9.8',"speciality":"modeling"}
sreja = {'gender':'male','branch':'eee','rollnumber':'4','age':'48','g.p.a':'9.9',"speciality":"acting"}
rishitha = {'gender':'female','branch':'it','rollnumber':'5','age':'100','g.p.a':'10',"speciality":"writer"}
varsha = {'gender':'female','branch':'ssc','rollnumber':'6','age':'3','g.p.a':'9.7',"speciality":"poetry"}
name=(input("enter the student name = "))
print("details we have = gender,branch,roolnumber,age,g.p.a,speciality")
want=input("enter the detail you want = ")
if(name in a):
    if(want=="gender")or(want=="branch")or(want=="roolnumber")or(want=="age")or (want=="g.p.a")or (want=="speciality"):
        print(name[want])
    else:
        print("the deatil is not found")
else:
    print("the name is not in clg records")