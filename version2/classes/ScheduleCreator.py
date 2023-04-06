class ScheduleCreator:
    def __init__(self,FoundClassObjList,generalPreferences,classList):
        self.FCobjList = FoundClassObjList
        self.generalPreferences = generalPreferences
        self.classList = classList
        self.neededCourses =  self.getNeededClasses()
        print(self.neededCourses)

    def getNeededClasses(self):
        neededCourses = []
        for neededClass in self.classList:
            tempList = []
            tempList.append(neededClass["cn"])
            tempList.append(neededClass["cc"])
            neededCourses.append(tempList)
        return neededCourses
        #self.neededCourses = neededCourses

    def convertTime(self,time):
        try:
            #print("here")
            hour = int(time[:2])
            meridian = time[6:]
            min = time[3:5]
        except:
            hour = int(time[:1])
            meridian = time[5:]
            min = time[2:4]
            #print(hour)
            #print(min)

            #meridian = time[5:]
            #meridian = time[:2]
            # Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
            if (hour == 12):
                hour = 0
            if (meridian == 'PM'):
                hour += 12
        return [hour,min]


    def compareTimes(self,begin_time,end_time,check_time):
        #returns true/false
        check_time = check_time #or datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time


    def checkMostIdeal(self):
        mostIdealCourses = []
        #index = 0
        for classType in self.FCobjList:
            #print(classType)
            for course in classType.foundClasses:
                #print(course)
                if course["accuracyList"][0]["status"]:
                    print("Most Ideal Course Found")
                    #index+=1
                    mostIdealCourses.append([course,classType.subject,classType.courseCode])

                else:
                    #index+=1
                    print("Not a most Ideal course")
                    #print(False)
                #print(course["accuracyList"][0])
                #if course["accuracyList"][0]:
                    #pass
                #print(course)
                #if(course.)
        self.mostIdealCourses = mostIdealCourses
        print(self.mostIdealCourses)
        #print(index)
    def createScheds(self):
        #print(self.mostIdealCourses)
        schedLists = []

        classSubjects =[]

        tempList=[]
        print("\n\n")
        for foundClass in self.mostIdealCourses:
            #print("\n\n")
            #print(foundClass)
            #print("\n\n")
            addedClasses = []
            if foundClass in tempList:
                #pass
                print("AlreadyInList")
            else:
                index=0
                for tempClass in tempList:
                    #not running
                    print("------------------------------------------------")
                    print(index)
                    print(foundClass[1])
                    print(tempClass)
                    print("------------------------------------------------")
                    index+=1
                    if(foundClass[1]) == tempClass[1]:
                        print("Course Code already in List")
                        addedClasses.append(foundClass[1])
                if foundClass[1] not in addedClasses:
                    tempList.append(foundClass[1])
        print(tempList)


                #print("AlreadyInList")
                #if condition:
                    #pass
                #print(foundClass)
            #foundClass.check_time()


        #out of for loop
