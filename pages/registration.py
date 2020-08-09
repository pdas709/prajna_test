from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from testingdata.staticinput import Testdata
from testingdata.readfromexcel import ReadWriteExcel

class HomePageObjectClass:    
   
    REGBUTTON=(By.XPATH,"//a[contains(.,'REGISTER')]")
    FIRSTNAME = (By.XPATH,"//input[@name='firstName']")
    LASTNAME = (By.XPATH,"//input[@name='lastName']")
    PHONEBUTTON=(By.XPATH,"//input[@name='phone']") 
    EMAIL=(By.XPATH,"//input[@id='userName']") 
    ADDRESS=(By.XPATH,"//input[@name='address1']") 
    CITY=(By.XPATH,"//input[@name='city']")
    STATE=(By.XPATH,"//input[@name='state']")
    POSTALCODE=(By.XPATH,"//input[@name='postalCode']")
    USERNAME= (By.XPATH,"//input[@id='email']")
    PASSWORD=(By.NAME,"password") 
    CONFIRMPASSWORD=(By.XPATH,"//input[@name='confirmPassword']") 
    SUBMIT=(By.XPATH,"//input[@name='submit']") 
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(ReadWriteExcel.readandADDurl(self)) 
       

    def clickreg(self):
        registrationbutton= self.browser.find_element(*self.REGBUTTON)
        registrationbutton.click()


    def registration(self):
        firstname = self.browser.find_element(*self.FIRSTNAME)
        #searchfield1.send_keys(Keys.CONTROL + 'a')
        firstname.send_keys(Testdata.firstname)
        lastname = self.browser.find_element(*self.LASTNAME)
        lastname.send_keys(Testdata.lastname)
        phonenumber = self.browser.find_element(*self.PHONEBUTTON)
        phonenumber.send_keys(Testdata.phonenumber)
        emailaddress = self.browser.find_element(*self.EMAIL)
        emailaddress.send_keys(Testdata.emailaddress)
        address = self.browser.find_element(*self.ADDRESS)
        address.send_keys("Masijbanda")
        city= self.browser.find_element(*self.CITY)
        city.send_keys("hyderabad")
        postalcode=self.browser.find_element(*self.POSTALCODE)
        postalcode.send_keys("500063")
        username= self.browser.find_element(*self.USERNAME) 
        username.send_keys(ReadWriteExcel.username(self))

    def enterpassword(self):
        password1= self.browser.find_element(*self.PASSWORD)
        password1.send_keys(ReadWriteExcel.password(self))
        confirmpassword=self.browser.find_element(*self.CONFIRMPASSWORD)
        confirmpassword.send_keys(ReadWriteExcel.password(self))
        
    def click_submit(self):
        submit=self.browser.find_element(*self.SUBMIT)
        submit.click()
        
   