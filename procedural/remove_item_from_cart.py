# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

########## STEP 1: Open Browser ###############
driver = webdriver.Chrome()

########## STEP 2: Open Magento ###############
driver.get("https://magento.softwaretestingboard.com/")

########## STEP 3: User Click Radiant Tee Item ###############

radiant_tee_item = driver.find_element(By.XPATH, "//img[@alt='Radiant Tee']")
radiant_tee_item.click()

########## STEP 4: User Select Item Size ###############

xl_size = driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-170']")
xl_size.click()

########## STEP 5: User Select Item Colour ###############

orange_colour = driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-56']")
orange_colour.click()

########## STEP 6: User Click Add To Cart Button ###############

addtocart_button = driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']")
addtocart_button.click()

########## STEP 7: User Click Shopping Cart Icon Button ###############

shoppingcart_icon_button = driver.find_element(By.XPATH, "//a[@class='action showcart']")
shoppingcart_icon_button.click()

########## STEP 8: User Click Trash Icon Button ###############

trash_icon_button = driver.find_element(By.XPATH, "//a[@class='action delete']")
trash_icon_button.click()

########## STEP 9: User Click Okay Button ###############

okay_button = driver.find_element(By.XPATH, "//span[normalize-space()='OK']")
okay_button.click()



time.sleep(30)