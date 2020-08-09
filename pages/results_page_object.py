from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ResultsPageObjectClass:
    RESULTTEXT = (By.XPATH, '(//span[contains(.,"A certification is a credential that you earn to show that")])[2]')
   
    def __init__(self,browser):
        self.browser = browser

    def result_text(self):
        resulttext = self.browser.find_element(*self.RESULTTEXT).text
        return resulttext
        

        