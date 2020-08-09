from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePageObjectClass:
    URL = "http://www.google.com"
    SEARCHFIELD = (By.XPATH,"//input[@class='gLFyf gsfi']")
    SEARCHBUTTON = (By.XPATH,"//input[@class='gNO89b']")
    FEELLUCKYBUTTON=(By.XPATH,"(//input[@class='RNmpXc'])[2]") 

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