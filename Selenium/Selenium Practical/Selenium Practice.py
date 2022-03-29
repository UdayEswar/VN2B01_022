from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\Users\DELL\\Desktop\\VN2B01_Training\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.google.com/")
print(driver.title)
search = driver.find_element_by_name("q")
search.send_keys("scientistuday.blogspot.com")
search.send_keys(Keys.ENTER)

driver.get("https://scientistuday.blogspot.com")


