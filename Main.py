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
from Classroom import Classroom

##### DO NOT TO CHANGE THIS FILE
##### IT WORKS ON A VERY BASIC LEVEL
##### USE THIS AS A TEMPLATE TO BUILD BETTER, MORE EFFICENT VERSIONS



#works on a very basic level --> CREATE BETTER VERSIONS WITH SUPPORT FOR THE FOLLOWING
    # need to allow lab support
    # refactor it so it is much more efficient
    # add support for things other than day --> if they prefer professor or if they prefer
    # click duo button
    # click class year and class type (wrtr/engr/etc)




####   get user input




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
    pass





##################

webdriver = webdriver.Chrome(ChromeDriverManager().install())
#WebDriver driver = new ChromeDriver();
webdriver.get("https://my.smu.edu/psp/ps/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main");


f = open("data.json")
userInfo = json.load(f)
f.close()

userId = userInfo[0]["userId"]
password = userInfo[0]["password"]


firstUserIdXpath = '//*[@id="username"]'
firstPasswordXpath= '//*[@id="password"]'

loginXpath ='//*[@id="shib-login"]/form/fieldset/div[4]/button'


time.sleep(1)
webdriver.find_element_by_xpath(firstUserIdXpath).send_keys(userId)


webdriver.find_element_by_xpath(firstPasswordXpath).send_keys(password)
time.sleep(1)
webdriver.find_element_by_xpath(loginXpath).click()
time.sleep(3)
print("Done loading")

#print("You have 10 seconds to log into duo")
#for i in range(11):
#    print(10-i)
#    time.sleep(1)
#
#print("OUT OF TIME")

print("Please log into duo")
print("Once You are done and the page has loaded press enter ")
enter = input()


subjectXpath = '/html/body/div[1]/main/div/form/div/div[4]/div/div/div/input'
#c580f132-1a08-90da-a664-7905c06e3a53
catalogXpath = '/html/body/div[1]/main/div/form/div/div[5]/div/div/div/input'
searchXpath = '/html/body/div[1]/main/div/form/div/div[11]/button/span'

termSearch= '/html/body/div[1]/main/div/form/div/div[2]/div/div/div/input'
#a57c2e92-d189-08c0-9b6d-7951fa89e385
#/html/body/div[1]/main/div/form/div/div[4]/div/div/div/input
#/html/body/div[1]/main/div/form/div/div[4]/div/div/div/input
#//*[@id="app"]/main/div/form/div/div[4]
#//*[@id="app"]/main/div/form/div/div[4]
#//*[@id="app"]/main/div/form/div/div[4]
wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('//*[@id="main_iframe"]')))

#webdriver.find_element_by_xpath(termSearch).send_keys("Spring 2022")

#print("What term? ")
#term =input()
#select = Select(webdriver.find_element_by_xpath(termSearch))
#select.select_by_visible_text(term)



#webdriver.find_element_by_xpath(subjectXpath).send_keys("cs")
#webdriver.find_element_by_xpath(catalogXpath).send_keys("1342")


#print("Subject")
#subject = input()

#if subject == "cs":
#    subject = "CS - Computer Science"
#elif subject == "wrtr":
#    subject = "WRTR - Writing and Reasoning"

print("Select course term and subject, then press enter")
time.sleep(1)
enter = input()


#select = Select(webdriver.find_element_by_xpath(subjectXpath))
#webdriver.find_element_by_xpath(searchXpath).click()
#select by visible text
#select.select_by_visible_text(subject)

#b.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()


#webdriver.find_element_by_xpath(subjectXpath).send_keys("value",subject)


#webdriver.find_element_by_xpath(subjectXpath).send_keys(subject)
time.sleep(1)
webdriver.find_element_by_xpath(catalogXpath).send_keys(catNumber)





webdriver.find_element_by_xpath(searchXpath).click()
print("1")

print("Waiting to load...")
time.sleep(5)

print("2")
webdriver.switch_to.default_content()

#//*[@id="main_iframe"]
#/html/body/div[1]/iframe
print("3")
wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('/html/body/div[1]/iframe')))

print("4")
#/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/button/span/div/svg
#webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/button/span/div/svg/g/path[2]').click()

#should be the xpath of the entire list of classes
classString = webdriver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul").text
#print(classString)                            /html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/p/span[2]


#class list seems to properly hold each class in as a differnt in the list-->except for classList[0] -->this holds like 1/2 a class but classList[1] holds the class properly
classList = classString.split("-\n")
print(classList)


print("5")

classDict={}
for i in range(len(classList)):
    if i==False:
        #skip first element// not a real class
        pass
    else:
        number="class "+str(i)
        newClassList= classList[i].split("\n")
        classDict[number]=newClassList

print(classDict)
print("6")
#print(classDict)
#print('\n')
#exampleString = webdriver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/p/span[2]").text
#print(exampleString)


"""
f = open("sample.json", "w+")
json.dump(classDict, f)
f.close()
"""

#print("What ")
classList = []
index= 0
if len(classDict) == 1:
    print("There is only 1 section of this class")
    print("would you like to enroll?(y/n)")
    enroll = input()
    if enroll == "y":
        spot = "1"
        openXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div/div[1]"
        webdriver.find_element_by_xpath(openXpath).click()
        time.sleep(2)
        enrollXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div[2]/div/div/div/div[2]/div[5]/button/span"
        webdriver.find_element_by_xpath(enrollXpath).click()
        time.sleep(10)
        exit()
    else:
        pass
else:

    for i in classDict:
        if len(classDict[i]) < 18:
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
prefList = prefString.split(",")

print(daysList)
print(timesList)
print(prefList)

index = 0
print("")
print(classList[0].day)
for i in prefList:
    if i == "day":
        dayIndex=0
        for d in daysList:
            classIndex = 0
            for classObj in classList:

                if d == classObj.day:
                    print("Here")
                    #open the class then enroll
                    spot  = str(classIndex+1)

                    #open class
                    openXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div/div[1]"
                    webdriver.find_element_by_xpath(openXpath).click()
                    time.sleep(2)

                    #enroll
                    enrollXpath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+spot+"]/div/div[2]/div/div/div/div[2]/div[5]/button/span"
                    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[1]/div/div[2]/div/div/div/div[2]/div[5]/button/span
                    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[2]/div/div[2]/div/div/div/div[2]/div[5]/button/span
                    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[3]/div/div[2]/div/div/div/div[2]/div[5]/button/span

                    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[19]/div/div[2]/div/div/div/div[2]/div[5]/button/span



                    webdriver.find_element_by_xpath(enrollXpath).click()
                    #should be enrolled

                    #wait for enrollment results
                    time.sleep(10)
                classIndex +=1

    if i == "":
        pass


####### IF  NEED BE THE NEXT 3 LINES OF CODE CAN BE USED TO RE-ADD THE DELIMITER IF I NEED TO RESPLIT THE LIST
#d = ">"
#for line in all_lines:
#    s =  [e+d for e in line.split(d) if e]




#/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[1]/div/div/div[1]
#/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[2]/div/div/div[1]
#/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[3]/div/div/div[1]






#/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul




#webdriver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul")




#counter = 1
#while True:
                    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/button/span/div/svg
    #elementXpath = f'/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[{counter}]/div/div/div[1]/div[1]/button/span/div/svg'
    #webdriver.find_element_by_xpath(elementXpath).click()
    #print(counter)
    #counter += 1

#print("You have 10 seconds to place a search- Do not press enter")//*[@id="main_iframe"]
#for i in range(11):
#    print(10-i)
#    time.sleep(1)


##INPUTS CANNOT BE FOUND - GIVE THE USER TIME TO SEARCH

#submitButtonXpath='//*[@id="app"]/main/div/form/div/div[11]/button/span'
#webdriver.find_element_by_xpath(submitButtonXpath).click()



#/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/button/span/div/svg/g/path[2]
#/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/button/span/div/svg/g/path[2]
