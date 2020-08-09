from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePageObjectClass:
    URL = "http://demo.guru99.com/test/newtours/login.php"
    USERNAME = (By.XPATH,"//input[@name='userName']")
    PASSWORD = (By.XPATH,"//input[@name='password']")
    SUBMITBUTTON=(By.XPATH,"(//input[@name='submit']") 

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL) 

    def searchtext(self):
        searchfield1 = self.browser.find_element(*self.SEARCHFIELD)
        #searchfield1.send_keys(Keys.CONTROL + 'a')
        searchfield1.send_keys("certifications")
        
    def searchbutton(self):
        searchbutton = self.browser.find_element(*self.SEARCHBUTTON)
        searchbutton.click()

    def feellucky(self):
        feelluckybutton = self.browser.find_element(*self.FEELLUCKYBUTTON)
        feelluckybutton.click()   