

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Set the path to your ChromeDriver executable
chrome_driver_path = "X/chromedriver-win64/chromedriver.exe"

# Launch the Chrome browser
driver = webdriver.Chrome()

# Launch the Application Under Test (AUT)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

# Right click the button to launch right-click menu options
actions = ActionChains(driver)

link = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")
actions.context_click(link).perform()

# Click on Edit link on the displayed menu options
element = driver.find_element(By.CSS_SELECTOR, ".context-menu-icon-copy")
element.click()

# Accept the alert displayed
# driver.switch_to.alert.accept()

# Closing the driver instance
# driver.quit()
