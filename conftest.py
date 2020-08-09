import pytest
from selenium.webdriver import Chrome

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