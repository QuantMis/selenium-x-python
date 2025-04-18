# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

########## STEP 1: Open Browser ###############
driver = webdriver.Chrome()

########## STEP 2: Open Magento ###############
driver.get("https://magento.softwaretestingboard.com/")

########## STEP 3: Click Create Account hyperlink ###############

create_account_link = driver.find_element(By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
create_account_link.click()

########## STEP 4: User Fill In First Name Input ###############

firstname_input = driver.find_element(By.ID, "firstname")
dummy_firstname = "nur"
firstname_input.send_keys(dummy_firstname)

########## STEP 5: User Fill In Last Name Input ###############

lastname_input = driver.find_element(By.ID, "lastname")
dummy_lastname = "alia"
lastname_input.send_keys(dummy_lastname)

########## STEP 6: User Fill In Email Input ###############

email_input = driver.find_element(By.ID, "email_address")
dummy_email = "test@gmail.com"
email_input.send_keys(dummy_email)


########## STEP 7: User Fill In Password Input ###############

password_input = driver.find_element(By.ID, "password")
dummy_password = "Abc12345def"
password_input.send_keys(dummy_password)

########## STEP 8: User Fill In Password Confirmation Input ###############

passwordconfirmation_input = driver.find_element(By.ID, "password-confirmation")
dummy_passwordconfirmation = "Abc12345def"
passwordconfirmation_input.send_keys(dummy_passwordconfirmation)


########## STEP 9: User Click Create Button ###############
create_account_button = driver.find_element(By.XPATH, "//button[@title='Create an Account']")
create_account_button.click();

time.sleep(30)
