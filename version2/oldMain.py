from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests
import json
import bs4
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from classes.Classroom import Classroom
from classes.Enroll import Enroll
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#getting user input## -Add json support

print("Type in classes or submit a json? (type/json) ")
method = input()
while method != "type" and method != "json":
    print("Type in classes or submit a json? (type/json) ")
    method = input()

if method == "type":

    print("What day(s) do you want to take the class? MoWeFr,MoWe,TuTh,etc")
    print("Input as many as you would like starting with most wanted to least wanted, seperated by commas")

    days = input()

    print("What start time would you like to take the class?")
    print("Input as many as you would like starting with most wanted to least wanted, seperated by commas")
    print("Please enter them in the form 8:00 am")
    times = input()

    print("Who is your most prefered professor? ")
    prefProf = input()

    print("Who which professor do you not want? ")
    badProf = input()

    print("Ranked from most to least importance, which of the above catigories do you value?")
    print("Please seperate your input with commas")
    print("If a catergory is irrelevent, do not include it")
    print("Example 1: day,wanted professor, not wanted professor,time")
    print("Example 2: not wanted professor,time,wanted professor,day")
    prefString = input()


#    print("Are there any categories you do not care about?(These will not be considered) ")
#    print("Please list them with commas")

    print("Catalog Number? Example if you want wrtr 1313, type 1313 ")
    catNumber = input()


else:
    #ask for a json file
    print("What is the filename?")
    fileName = input()
    fileName += ".json"
    f = open(fileName)
    personInfo = json.load(f)
    f.close()

    days = personInfo["days"]
    term = personInfo["term"]
    catNumber = personInfo["classCode"]
    userId = personInfo["userId"]
    password = personInfo["password"]
    times = personInfo["times"]
    course = personInfo["course"]





###############


### THE NEXT FEW LINES LOG INTO MY my.smu --> CANNOT GET CLICK DUO BUTTONS YET
#webdriver = webdriver.Chrome(ChromeDriverManager().install())
#WebDriver driver = new ChromeDriver();
#webdriver.get("https://my.smu.edu/psp/ps/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main");


link = "https://my.smu.edu/psp/ps/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main"
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
webdriver.get(link);





#f = open("data.json")
#userInfo = json.load(f)
#f.close()

#userId = userInfo[0]["userId"]
#password = userInfo[0]["password"]


firstUserIdXpath = '//*[@id="username"]'
firstPasswordXpath= '//*[@id="password"]'

loginXpath ='//*[@id="shib-login"]/form/fieldset/div[4]/button'


time.sleep(1)

webdriver.find_element(By.XPATH, firstUserIdXpath).send_keys(userId)
#webdriver.find_element_by_xpath(firstUserIdXpath).send_keys(userId)


webdriver.find_element(By.XPATH, firstPasswordXpath).send_keys(password)
#webdriver.find_element_by_xpath(firstPasswordXpath).send_keys(password)
time.sleep(1)
webdriver.find_element(By.XPATH, loginXpath).click()
#webdriver.find_element_by_xpath(loginXpath).click()
time.sleep(3)
print("Done loading")


### WAITS FOR DUO
print("Please log into duo")
print("Once You are done and the page has loaded press enter ")
enter = input()




###
#required xpaths
subjectXpath = '/html/body/div[1]/main/div/form/div/div[4]/div/div/div/input'
catalogXpath = '/html/body/div[1]/main/div/form/div/div[5]/div/div/div/input'
searchXpath = '/html/body/div[1]/main/div/form/div/div[11]/button/span'
termSearch= '/html/body/div[1]/main/div/form/div/div[2]/div/div/div/input'



#gets into the iframe
wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('//*[@id="main_iframe"]')))


#user has to activly select --> change this
#print("Select course term and subject, then press enter")
#time.sleep(1)
#enter = input()
#wait a second to load


###Still working on this part
#webdriver.find_element(By.XPATH, termSearch).send_keys("Spring 2022")
#webdriver.find_element(By.XPATH, termSearch).send_keys(Keys.DOWN)
#time.sleep(1)
#######


#selects the course subject (wrtr, etc)
webdriver.find_element(By.XPATH, subjectXpath).send_keys(course)
webdriver.find_element(By.XPATH, subjectXpath).send_keys(Keys.DOWN)


time.sleep(1)



#type in the catalog number then enter it
webdriver.find_element(By.XPATH, catalogXpath).send_keys(catNumber)
webdriver.find_element(By.XPATH, searchXpath).click()
#webdriver.find_element_by_xpath(catalogXpath).send_keys(catNumber)
#webdriver.find_element_by_xpath(searchXpath).click()

#waits for the classes to load
print("Waiting to load...")
time.sleep(5)

#exits then reenters the iframe
webdriver.switch_to.default_content()
wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('/html/body/div[1]/iframe')))

###grabs all the classes availible in the section then creates a list of them
#classString = webdriver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul").text
webdriver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul").text
classList = classString.split("-\n")


### turns the list into a dictionary
classDict={}
for i in range(len(classList)):
    if i==False:
        #skip first eleemnt// not a real class
        pass
    else:
        number="class "+str(i)
        newClassList= classList[i].split("\n")
        classDict[number]=newClassList



### begins the logic --> make this class based or something so it runs much more efficeintly
classList = []
index= 0
if len(classDict) == 1:
    #if there is only one class in the section it acts weird
    #this instant enrolls
    print("There is only 1 section of this class")
    print("would you like to enroll?(y/n)")
    enroll = input()
    if enroll == "y":
        #this was never made into a ClassRoom obj so the enroll method cannot be called
        spot = "1"
        openXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div/div[1]"
        webdriver.find_element(By.XPATH, openXpath).click()
        #webdriver.find_element_by_xpath(openXpath).click()
        time.sleep(2)
        enrollXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div[2]/div/div/div/div[2]/div[5]/button/span"
        webdriver.find_element(By.XPATH, enrollXpath).click()
        #webdriver.find_element_by_xpath(enrollXpath).click()
        time.sleep(10)

        #kills the process, possibly change this so that it will try to enroll in multiple classes
        exit()
    else:
        pass
else:

    for i in classDict:
        if len(classDict[i]) < 18:
            #sometimes it will be less than 18 items so it must go through this
            #turns it into a class object
            foundClass = classDict[i]
            seats = foundClass[14].split(" ")
            if seats[0][:-1] == "Open":
                isOpen = True
            else:
                isOpen=False

            classSect = foundClass[15].split(" ")
            lecSec = classSect[2]
            classNum = classSect[4][-4:]
            classObj = Classroom(foundClass[3],foundClass[4],foundClass[6],foundClass[8][:len(foundClass[8])-4], foundClass[8][-4:],foundClass[12],isOpen,seats[1],seats[3],lecSec,classNum)

        else:
            #regular amout of items it turns it into a class object
            foundClass = classDict[i]
            print(foundClass)
            seats = foundClass[14].split(" ")

            classSect = foundClass[17].split(" ")
            if seats[0][:-1] == "Open":
                isOpen = True
            else:
                isOpen=False
                                            #day,startTime,endTime,building,room,prof,isOpen,seatsOpen,totalSeats,lecSec,classNum
            classObj = Classroom(foundClass[3],foundClass[4],foundClass[6],foundClass[8][:len(foundClass[8])-4], foundClass[8][-4:],foundClass[12],isOpen,seats[1],seats[3],classSect[2],classSect[4][-4:])

            classList.append(classObj)


        index +=1
    #print(classList[0])

#these are user defined of what is prefered
daysList = days.split(",")
timesList = times.split(",")
prefList = prefString.split(",") #ordered list of what the user wants


#
index = 0
#print("")
#print(classList[0].day)

#begins to enroll in the class when the proper conditions are met
for i in prefList:
    if i == "day":
        dayIndex=0
        for d in daysList:
            classIndex = 0
            for classObj in classList:

                if d == classObj.day:
                    classObj.enroll(classIndex)
                classIndex +=1




    if i == "profGood":
        for classObj in classList:
            if classObj:
                pass
