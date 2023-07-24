from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = driver.find_element_by_id("search")
element.send_keys("bear")


btn = driver.find_element_by_id("loginbtn")
btn.click()



#html/body/div[1]/div[2]/div/div/section/div/div/div/div/div[1]/div[1]/div/div[2]/div/a
