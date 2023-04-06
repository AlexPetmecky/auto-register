import json
from classes.TestClass import TestClass
from classes.NewTest import NewTest
f = open("sample.json")
data = json.load(f)
f.close()

obj1 = NewTest("hello")
print(obj1.name)
#for i in data:
#print(data["class 1"][8][-4:])
#[8][:len(data[8])-4]
#foundClass[8][:len(foundClass[8])-4]

obj = TestClass("John")
print(obj.name)

"""
print(data["class 1"])
for i in range(len(data["class 1"])):
    print(str(i) +": "+str(data["class 1"][i]))

lista = ["a","b","c"]
print(len(lista))
"""



"""
index=0

for i in lista:
    if index == len(lista)-1:
        pass
    else:
        print(i)
    index+=1
"""


data = "abc"
data2 = "a,b,c"

lista = data.split(",")
listb = data2.split(",")
print(lista)
print(listb)
#seats = data["class 1"][17].split(" ")
#print(seats[4][-4:])


#print(seats[0][:-1])
#classObj = Classroom("test")
#classObj.giveName()
