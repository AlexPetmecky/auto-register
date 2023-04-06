import json
from classes.TestClass import TestClass
from classes.NewTest import NewTest
from datetime import time

def convertTime(time):
    try:
        #print("here")
        hour = int(time[:2])
        meridian = time[6:]
        min = int(time[3:5])
    except:
        hour = int(time[:1])
        meridian = time[5:]
        min = int(time[2:4])
        #print(hour)
        print(min)

        #meridian = time[5:]
        #meridian = time[:2]
        # Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
    if (hour == 12):
        hour = 0
    if (meridian == 'PM'):
        hour += 12
    return [hour,min]


def compareTimes(begin_time,end_time,check_time):
    check_time = check_time #or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time







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


print(len(lista))
"""
lista = ["a","b","c"]
for i in lista:
    print(i)


"""
index=0

for i in lista:
    if index == len(lista)-1:
        pass
    else:
        print(i)
    index+=1
"""




"""
try:
    print("here")
    hour = int(time[:2])
    meridian = time[6:]
    min = int(time[3:5])
except:
    hour = int(time[:1])
    meridian = time[5:]
    min = int(time[2:4])
#print(hour)
print(min)

#meridian = time[5:]
#meridian = time[:2]
# Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
if (hour == 12):
    hour = 0
if (meridian == 'PM'):
    hour += 12
"""
#milTime = [hour,min]
#print([hour,min])
#myTime = "8:20 PM"
times = ["8:20 AM","12:00 PM","8:30 AM"]
newTimes = []
for i in times:
    newTimes.append(convertTime(i))
print(newTimes)
print(compareTimes(newTimes[0],newTimes[1],newTimes[2]))
#print(time(newTime[0],newTime[1]))



#print("%02d" % hour + time[2:8])



#seats = data["class 1"][17].split(" ")
#print(seats[4][-4:])


#print(seats[0][:-1])
#classObj = Classroom("test")
#classObj.giveName()
