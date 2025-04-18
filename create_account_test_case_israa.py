# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

########## STEP 1: Open Browser ###############
driver = webdriver.Chrome()

########## STEP 2: Open Magento ###############
driver.get("https://magento.softwaretestingboard.com/")

########## STEP 3: Click Create Account hyperlink ###############
# Detail: 1) Locate the element using selenium
#         2) Click the element using selenium

# bagi criteria element dekat selenium, supaya dia boleh cari
# 1) Kita cari element <a>
# 2) Kita dapat banyak element <a>
# 3) Kita pilih element <a> yang kedua sebab itu yang kita nak
# 4) Kita click element yg kita pilih tu

all_anchors_element = driver.find_elements(By.TAG_NAME, "a")
create_account_anchor = all_anchors_element[2]
create_account_anchor.click()
time.sleep(5)


########## STEP 4: User Fill In First Name Input ###############

# 1) Kita cari element username input 
firstname_input = driver.find_element(By.ID, "firstname")
# 2) Kita declare variable to store username value
dummy_firstname = "nur"
# 3) Masukkan value to firstname input
firstname_input.send_keys(dummy_firstname)

########## STEP 5: User Fill In Last Name Input ###############
# 1) Kita cari element username input 
lastname_input = driver.find_element(By.ID, "lastname")
# 2) Kita declare variable to store username value
dummy_lastname = "alia"
# 3) Masukkan value to firstname input
lastname_input.send_keys(dummy_lastname)

########## STEP 6: User Fill In Email Input ###############

email_input = driver.find_element(By.ID, "email_address")
dummy_email = "test@gmail.com"
email_input.send_keys(dummy_email)

########## STEP 7: User Fill In Password Input ###############

password_input = driver.find_element(By.ID, "password")
dummy_password = "Abc123456def"
password_input.send_keys(dummy_password)

########## STEP 8: User Fill In Password Confirmation Input ###############

passwordconfirmation_input = driver.find_element(By.ID, "password-confirmation")
dummy_passwordconfirmation = "Abc12345def"
passwordconfirmation_input.send_keys(dummy_passwordconfirmation)


time.sleep(30)
