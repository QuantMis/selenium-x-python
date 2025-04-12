from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Or use Firefox()
driver.get("https://magento.softwaretestingboard.com/")

# Find an element and interact
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

driver.quit()
