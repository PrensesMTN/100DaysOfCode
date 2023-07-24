#   Selenium and Webdriver

In Day Two ı found a otomatic Chrome image downloader module but it didnt work properly so ı want to make my own  
Selenium is a portable framework for testing web applications, which provides an API to automate various browsers like. 

## installation

```
pip install selenium
```
And you have to install webdriver for Chrome and geckodriver


## Simple code
```python

from selenium import webdriver
from selenium.webdriver import ActionChains

# Set the path to your ChromeDriver executable
chrome_driver_path = "X/chromedriver-win64/chromedriver.exe"

# Launch the Chrome browser
driver = webdriver.Chrome()

# Launch the Application Under Test (AUT)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

```

## Usage

If you make installation fine then open a python IDE and run code
I will test my code on [TEST WEB](https://demo.guru99.com/test/simple_context_menu.html)
