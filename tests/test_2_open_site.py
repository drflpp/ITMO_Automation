from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

icon = driver.find_element(By.CSS_SELECTOR, "header > a > img")

if icon is None:
    print('Element is not found')

else:
    print('Element is found')