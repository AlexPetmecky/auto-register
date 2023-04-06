####NOTES
 #incorperate the generalPreferences (new section in json-->look for it ) into the code somewhere
    # -->probably in the ScheduleCreator class

#in the foundClasses

#######
#MAKE A 3RD VERSION THAT PUTS EACH OF THE FOUNDCOURSE IN ITS WON OBJECT OF A CLASS INSTEAD OF HAVING AN OBJECT CAINTING ALL THE COURSE OPTIONS FOUND FOR A SPECIFIC SUBJECT

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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from classes.Course import Course
#from classes.Classroom import Classroom
#from classes.Enroll import Enroll
#from classes.FoundClasses import FoundClasses
#from classes.ScheduleCreator import ScheduleCreator
print(Course("classList","subject","catNumber"))
#print("What is the filename?")
#fileName = input()
fileName = "alex"
#temporarily do not ask for filename, just use alex
fileName += ".json"
f = open(fileName)
personInfo = json.load(f)
f.close()

userId = personInfo["userId"]
password = personInfo["password"]
classDictsList = personInfo["courselist"]
generalPreferences = personInfo["genPref"]
#print(len(classDictsList))
link = "https://my.smu.edu/psp/ps/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main"
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
webdriver.get(link);

#
firstUserIdXpath = '//*[@id="username"]'
firstPasswordXpath= '//*[@id="password"]'

loginXpath ='//*[@id="shib-login"]/form/fieldset/div[4]/button'


time.sleep(1)

webdriver.find_element(By.XPATH, firstUserIdXpath).send_keys(userId)


webdriver.find_element(By.XPATH, firstPasswordXpath).send_keys(password)
time.sleep(1)
webdriver.find_element(By.XPATH, loginXpath).click()

time.sleep(3)
print("Done loading")


print("Please log into duo")
duoIframe ='/html/body/div/div/div/div[2]/div[1]/div/iframe'
wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element(By.XPATH, duoIframe)))

duoXpath = '//*[@id="auth_methods"]/fieldset/div[1]/button'
webdriver.find_element(By.XPATH, duoXpath).click()
time.sleep(1)
webdriver.switch_to.default_content()
time.sleep(5)
print("Once You are done and the page has loaded press enter ")
enter = input()

foundCourseDict = {}
classesList = []
counter = 0
CourseList=[]

for userGivenClass in classDictsList:
    # will go through and find all the classes availible for the section
    #at the end of the loop it needs to go to the search page of the site
    subject = userGivenClass["cn"]
    catNumber = userGivenClass["cc"]
    #required xpaths
    subjectXpath = '/html/body/div[1]/main/div/form/div/div[4]/div/div/div/input'
    catalogXpath = '/html/body/div[1]/main/div/form/div/div[5]/div/div/div/input'
    searchXpath = '/html/body/div[1]/main/div/form/div/div[11]/button/span'
    termSearch= '/html/body/div[1]/main/div/form/div/div[2]/div/div/div/input'


    #gets into the iframe

    #webdriver.find_element(By.XPATH, '//*[@id="main_iframe"]')
    #time.sleep()
    wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element(By.XPATH, '//*[@id="main_iframe"]')))
    #wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('//*[@id="main_iframe"]')))
    print("PAST LINE 80")

    #selects the course subject (wrtr, etc)
    webdriver.find_element(By.XPATH, subjectXpath).send_keys(subject)
    webdriver.find_element(By.XPATH, subjectXpath).send_keys(Keys.DOWN)


    time.sleep(1)



    #type in the catalog number then enter it
    webdriver.find_element(By.XPATH, catalogXpath).send_keys(catNumber)


    #hits the search button
    webdriver.find_element(By.XPATH, searchXpath).click()


    print("Waiting to load...")
    time.sleep(5)

    #exits then reenters the iframe
    webdriver.switch_to.default_content()
    wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element(By.XPATH, '/html/body/div[1]/iframe')))

#    wait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it(webdriver.find_element_by_xpath('/html/body/div[1]/iframe')))


    ###grabs all the classes availible in the section then creates a list of them
    index=1
    print("=========================================================")
    while(True):
        #classXPath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+str(index)+"]/div/div"
        #classString = webdriver.find_element(By.XPATH,classXPath ).text
        #classList = classString.split("-\n")
        #print(classList)
        #data=Course(classList,subject,catNumber)
        #print(data)
        #CourseList.append(data)
        #index +=1
        try:
            classXPath = "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div["+str(index)+"]/div/div"
            classString = webdriver.find_element(By.XPATH,classXPath ).text
            classList = classString.split("-\n")
            print(classList)
            data=Course(classList,subject,catNumber)
            #print(data)
            CourseList.append(data)
            #print("---------------------------------")
            #print(CourseList)
            #print("---------------------------------")
            index +=1
        except:
            break

    #classString = webdriver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[1]/div/div").text
    #print(classString)
    #classList = classString.split("-\n")
    #print(classList)
    print("=========================================================")
    #redirect to the link so the code keeps working in the loop
    webdriver.get(link);

    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/li[23]
    #/html/body/div[1]/main/div/div/div[2]/div/div[2]/ul/div[THIS SHOULD BE THE ELEMENT THAT STARTS AT ONE, USE A TRY EXCEPT TO LOOP THROUGH NUMBERS UNTIL IT CANNOT FIND MORE COURSE]/div/div
    #print(classString)
    #classList = classString.split("-\n")
    #print(classList)
    #cleanClassList = []
    ### turns the list into a dictionary

print(CourseList[0].cleanList)
