# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://magento.softwaretestingboard.com/"

# element locators
sign_in_link = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
email_input = (By.ID, "email")
password_input = (By.ID, "pass")
sign_in_button = (By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")

# input value
dummy_firstname = "nur"
dummy_email = "test@gmail.com"
dummy_password = "Abc12345def"


# process
driver = webdriver.Chrome()
driver.get(url)


driver.find_element(*sign_in_link).click()
driver.find_element(*email_input).send_keys(dummy_email)
driver.find_element(*password_input).send_keys(dummy_password)
driver.find_element(*sign_in_button).click()