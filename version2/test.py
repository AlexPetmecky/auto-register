
from classes.FoundClasses import FoundClasses
from classes.ScheduleCreator import ScheduleCreator
import json
with open("alex.json","r") as f:
    myData = json.load(f)
f.close()

with open("sample.json","r") as f:
    classData = json.load(f)
f.close()

#print(myData)

myObj = FoundClasses(myData["courselist"][0]["cn"],myData["courselist"][0]["cc"],classData,myData["courselist"][0],True)
#myObj.addAccuracyList()
#myObj.giveXpathNumber()
#print(myObj.foundClasses)
#myObj.subject
newObj = ScheduleCreator(myObj.foundClasses)
newObj.checkMostIdeal()
