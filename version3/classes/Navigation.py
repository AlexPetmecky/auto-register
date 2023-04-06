#FILE IS UNUSED
#DONT EVEN IMPORT IT MAY FIX IT IN A LATER VERSION
class Navigation:
    def __init__(self,link):
        self.link = link

    def login(self):
        webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        webdriver.get(self.link);

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

    def navToClass(self,subject,catNumber):
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
