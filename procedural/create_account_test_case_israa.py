# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://magento.softwaretestingboard.com/"

# element locators
create_account_link = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
firstname_input = (By.ID, "firstname")
lastname_input = (By.ID, "lastname")
email_input = (By.ID, "email_address")
password_input = (By.ID, "password")
passwordconfirmation_input = (By.ID, "password-confirmation")
create_account_button = (By.XPATH, "//button[@title='Create an Account']")


# input value
dummy_firstname = "nur"
dummy_lastname = "alia"
dummy_email = "test@gmail.com"
dummy_password = "Abc12345def"
dummy_passwordconfirmation = "Abc12345def"

# process
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(*create_account_link).click()
driver.find_element(*firstname_input).send_keys(dummy_firstname)
driver.find_element(*lastname_input).send_keys(dummy_lastname)
driver.find_element(*email_input).send_keys(dummy_email)
driver.find_element(*password_input).send_keys(dummy_password)
driver.find_element(*passwordconfirmation_input).send_keys(dummy_passwordconfirmation)
driver.find_element(*create_account_button).click()





