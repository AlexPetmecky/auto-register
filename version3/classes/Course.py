class Course:
    def __init__(self,courseList,courseSubject,courseCatNumber,xPathNumber):
        self.courseList = courseList
        self.courseSubject = courseSubject
        self.courseCatNumber = courseCatNumber
        self.xPathNumber = xPathNumber
        self.cleanList=[]
        self.classDict
        self.makeClassDict()
        self.convertToCleanList()

        #self.cleanList = self.convertToCleanList()

    def convertToCleanList(self):
        newList =[]
        itemsList=[]
        for elem in self.courseList:
            tempList=[]
            tempList.append(elem.split("\n"))
            for item in tempList:
                itemsList.append(item)

        #newList.append(newList)
        for listItem in itemsList:
            for info in listItem:
                newList.append(info)
        newList.append(self.courseSubject)
        newList.append(self.courseCatNumber)
        newList.append(self.xPathNumber)
        self.cleanList = newList
        #return newList

        def makeClassDict(self):
            #currently working on this
            courseList =self.courseList
            classDict = {"lecSec":courseList[0],
                        "classNum":courseList[1][-4:],
                        "day":courseList[6],
                        "startTime":courseList[7],
                        "endTime":courseList[9],
                        "location":courseList[11][:-5],
                        "prof":courseList[15],
                        "subject":courseList[19],
                        "catNumber":courseList[20],
                        "xPathNum":courseList[21]
                        };
            self.classDict = courseList
