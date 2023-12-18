from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://catalog.apps.asu.edu/catalog/classes")
    
    # Closes the ask for cookies by clicking the close button
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Close']")))
    close_button.click()
    
    # Enter Input For Subject
    subject_input = wait.until(EC.element_to_be_clickable((By.NAME, 'subject')))
    subject_input.click()
    subject_input.send_keys('CSE')
    
    # Enter Input For Number
    number_input = wait.until(EC.element_to_be_clickable((By.NAME, 'catalogNbr')))
    number_input.click()
    number_input.send_keys('355')
    
    # Click the Search button
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "search-button")))
    search_button.click()

finally:
    driver.quit()
