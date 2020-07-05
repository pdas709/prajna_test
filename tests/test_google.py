import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
  # Initialize ChromeDriver
  driver = Chrome()
  driver.maximize_window()
  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  # Return the driver object at the end of setup
  yield driver
  # For cleanup, quit the driver
  driver.quit()

def test_google_search(browser):
  # Set up some test case data
  URL = 'https://www.google.com'
  # Navigate to the DuckDuckGo home page
  browser.get(URL)

  assert browser.title == "Google"
  time.sleep(5)

  search_field = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
  search_field.click()
  search_field.send_keys('Football' + Keys.ENTER)
  time.sleep(5)