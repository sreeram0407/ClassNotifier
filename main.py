from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
try:
    driver.get("https://catalog.apps.asu.edu/catalog/classes")
    time.sleep(5)
    subject_input = driver.find_element(By.NAME, 'Subject')
    subject_input.click()
    subject_input.send_keys('CSE')
    time.sleep(5)
    
    number_input = driver.find_element(By.NAME, 'Number')
    number_input.click()
    number_input.send_keys('355')
    time.sleep(5)
    
    search_button = driver.find_element(By.NAME, 'search-button')
    search_button.click()
    

finally:
    driver.quit()