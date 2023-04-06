class FoundClasses:

    def __init__(self,subject,courseCode,foundClasses,givenCourse,isOnlyClassAvailible):
        #course is a list contianing the user input about a couse
        self.subject = subject
        self.courseCode = courseCode

        #foundClasses is a list of the classes
        self.foundClasses = foundClasses
        #givenCourse is a list
        self.givenCourse = givenCourse
        self.isOnlyClassAvailible = isOnlyClassAvailible

    def turnListToDict(self):
        #crashes if the course found is already enrolled in

        #turns a class list into a dictionary
        #individualClassDict = {"days":foundClass[3],"startTime":foundClass[4],"endTime":foundClass[6],"building"foundClass[8][:len(foundClass[8])-4],"room":foundClass[8][-4:],"prof":foundClass[12],"isOpen":isOpen,"seatsOpen":seats[1],"totalSeats":seats[3],"lecSec":classSect[2],"classNum":classSect[4][-4:]}

        totalClassList=[]

        for classItem in self.foundClasses:

            if len(self.foundClasses[classItem]) < 18:
                #some of this code needs to be edited
                #the first class for math 1338 causes the error
                #i think its because i am enrolled in it already,
                #try switching code in the json file so that
                foundClass =self.foundClasses[classItem]
                #seats = foundClass[14].split(" ")
                seats = foundClass[15].split(" ")#this might not work for other classes
                if seats[0][:-1] == "Open":
                    isOpen = True

                else:
                    isOpen=False


                classSect = foundClass[15].split(" ")#this may need to be changed
                                                    #if the index is 16 it seems to break for some of the classes (not the last one)
                                                    #if the index is 15(LOGIC ERROR-NOT SYNTAX ERROR), it seems to pull incorrect information from the class,AT LEAST FOR THE LAST CLASS, UNSURE ABOUT ANYOTHER CLASSES
            else:
                foundClass = self.foundClasses[classItem]
                #print(foundClass)
                seats = foundClass[14].split(" ")


                classSect = foundClass[17].split(" ")
                if seats[0][:-1] == "Open":
                    isOpen = True
                else:
                    isOpen=False
            print("NEW CLASS LISTED")
            print("Subject ",self.subject)
            print("Course Code ",self.courseCode)
            print("foundClass: ",foundClass)
            print("Seats",seats)
            print("classSect",classSect)

            #print()
            try:
                individualClassDict = {"days":foundClass[3],"startTime":foundClass[4],"endTime":foundClass[6],"building":foundClass[8][:len(foundClass[8])-4],"room":foundClass[8][-4:],"prof":foundClass[12],"isOpen":isOpen,"seatsOpen":seats[1],"totalSeats":seats[3],"lecSec":classSect[2],"classNum":classSect[4][-4:],"negProf":foundClass[12],"accuracyList":[]}
            except:
                individualClassDict = {"days":foundClass[3],"startTime":foundClass[4],"endTime":foundClass[6],"building":foundClass[8][:len(foundClass[8])-4],"room":foundClass[8][-4:],"prof":foundClass[12],"isOpen":isOpen,"seatsOpen":seats[1],"totalSeats":seats[3],"lecSec":classSect[2],"classNum":classSect[4][-4:],"negProf":foundClass[12],"accuracyList":[]}

            print("individualClassDict: ",individualClassDict)
            #print("PRODUCED ANOTHER individualClassDict")
            totalClassList.append(individualClassDict)

        return totalClassList


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
        check_time = check_time #or datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    def addAccuracyList(self):
        #adds an accuracyList containing dicts on whether or not a preference is met within a class

        prefList = self.givenCourse["preference"]
        #print(prefList)
        #the classes here have been found on my.smu
        classListOfDicts = self.turnListToDict()
        #print(classListOfDicts)
        #prefList is the list of preferences the person wants for the class
        for prefType in prefList:
            #crashes if the user puts ranks a preference in the list without actually giving the preference, ex putting prof in the preference list without adding a key value pair to the dict
            print(prefType)
            #pref is the item within the preflist that a person wants

            #actualPrefList is an array of what the person wants ex: the times or the days of the class they want (these have been given, they are not found)
            actualPrefList = self.givenCourse[prefType] #uses the preference as an index

            for foundClassDict in classListOfDicts:

                #classPrefItem = elem[pref]
                accuracyList = []

                for actualPref in actualPrefList:


                    if actualPref == foundClassDict[prefType]:
                        #this should look somehting like if 8:00 AM == 8:00 AM or if TuTh == TuTh

                        #if prefType = "negProf":
                            #accuracyList.append(-1)
                        #else:
                            #accuracyList.append(1)
                        accuracyDict = {prefType:actualPref,"status":True}


                    else:
                        #accuracyList.append(0)
                        accuracyDict = {prefType:actualPref,"status":False}
                    foundClassDict["accuracyList"].append(accuracyDict)
        #print(foundClassDict)
                    #print(accuracyDict)
                    #foundClassDict["accuracyList"].append(accuracyDict)
                    #print(individualClassDict)

                #foundClassDict["accuracyList"] = accuracyList
        #print(classListOfDicts)
        self.foundClasses = classListOfDicts
        #return classListOfDicts

        #for i in classListOfDicts:
        #    print(i)
        #    print("\n\n")
    def giveXpathNumber(self):
        index=1
        newList = []
        for foundClass in self.foundClasses:
            foundClass["xpathNumber"] = index
            newList.append(foundClass)
            index+=1
        self.foundClasses = newList
    def organizeClasses(self):

        #the second parameter is a massize dict of all the found classes along with all the accuracy ratings to the specific classes
        for i in dictOfClassListOfDicts:
            pass
