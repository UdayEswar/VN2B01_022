from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\Desktop\\VN2B01_Training\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("Uday Computer Service Center kakinada")
#driver.find_element(By.NAME)
#if element.text == 'Uday Computer Service Centre':
print(driver.title)


time.sleep(5)
#driver.quit()


