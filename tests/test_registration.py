import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from pages.registration import HomePageObjectClass
import time

def test_google_search(browser):
  # Set up some test case data
  home_page = HomePageObjectClass(browser)
  home_page.load()
  time.sleep(2)
  home_page.clickreg()
  home_page.registration()
  home_page.enterpassword()
  home_page.click_submit()
  





  
 
  '''URL = 'https://www.google.com'
  # Navigate to the DuckDuckGo home page
  browser.get(URL)
  time.sleep(10)
//verifying the title
  assert browser.title == "Google"
  time.sleep(5)

  search_field = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
  search_field.click()
  search_field.send_keys('Football' + Keys.ENTER)
  time.sleep(5)'''