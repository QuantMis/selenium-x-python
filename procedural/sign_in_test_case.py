# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

########## STEP 1: Open Browser ###############
driver = webdriver.Chrome()

########## STEP 2: Open Magento ###############
driver.get("https://magento.softwaretestingboard.com/")


########## STEP 3: Click Sign In hyperlink ###############

sign_in_link = driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
sign_in_link.click()

########## STEP 4: User Fill In Email Input ###############

email_input = driver.find_element(By.ID, "email")
dummy_email = "test@gmail.com"
email_input.send_keys(dummy_email)

########## STEP 5: User Fill In Password Input ###############

password_input = driver.find_element(By.ID, "pass")
dummy_password = "Abc12345def"
password_input.send_keys(dummy_password)

########## STEP 6: User Click Sign In Button ###############
sign_in_button = driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
sign_in_button.click();

time.sleep(30)
