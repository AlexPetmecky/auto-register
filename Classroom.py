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



    def __str__(self):
        return self.classNum
"""
    def __init__(self,name):
        self.name=name


    def giveName(self):
        print(self.name)
"""
