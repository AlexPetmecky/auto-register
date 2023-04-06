class Classroom:

    def __init__(self,day,startTime,endTime,building,room,prof,isOpen,seatsOpen,totalSeats,lecSec,classNum):
        self.day = day
        self.startTime =startTime
        self.endTime =endTime
        self.building=building
        self.room=room
        self.prof=prof
        self.isOpen =isOpen
        self.seatsOpen = seatsOpen
        self.totalSeats = totalSeats
        self.lecSec=lecSec
        self.classNum = classNum


    def enroll(self,index):
        spot = str(index+1)
        openXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div/div[1]"
        webdriver.find_element_by_xpath(openXpath).click()
        time.sleep(2)
        enrollXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div[2]/div/div/div/div[2]/div[5]/button/span"
        webdriver.find_element_by_xpath(enrollXpath).click()
        time.sleep(10)

    def getDemandNumber(self,prefList):
        #demand number will be created by associating
        for i in prefList:
            if i == "day":
                pass
            elif i == "":
                pass

        


    def __str__(self):
        #used as a test
        return self.classNum
