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


########## STEP 8: User Click Proceed to Checkout Button ###############

proceedtocheckout_button = driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']")
proceedtocheckout_button.click()

########## STEP 9: User Fill In Email Input ###############

email_input = driver.find_element(By.XPATH, "//div[@class='control _with-tooltip']//input[@id='customer-email']")
dummy_email = "faceheti@mailinator.com"
email_input.send_keys(dummy_email)


########## STEP 10: User Fill In First Name Input ###############

firstname_input = driver.find_element(By.XPATH, "//input[@id='UEK331I']")
dummy_firstname = "Madeson"
firstname_input.send_keys(dummy_firstname)


########## STEP 11: User Fill In Last Name Input ###############

lastname_input = driver.find_element(By.XPATH, "//input[@id='FP2KUT9']")
dummy_lastname = "Stuart"
lastname_input.send_keys(dummy_lastname)


########## STEP 12: User Fill In Company Name Input ###############

companyname_input = driver.find_element(By.XPATH, "//input[@id='Q805SOM']")
dummy_companyname = "Walls Hill Associates"
companyname_input.send_keys(dummy_companyname)


########## STEP 13: User Fill In Street Address Name (Line 1) Input ###############

streetaddressname_line1_input = driver.find_element(By.XPATH, "//input[@id='KOWB8K4']")
dummy_streetaddressname_line1 = "985 East Oak Parkway"
streetaddressname_line1_input.send_keys(dummy_streetaddressname_line1)

########## STEP 14: User Fill In Street Address Name (Line 2) Input ###############

streetaddressname_line2_input = driver.find_element(By.XPATH, "//input[@id='LHL2W3E']")
dummy_streetaddressname_line2 = "Est praesentium reru"
streetaddressname_line2_input.send_keys(dummy_streetaddressname_line2)


########## STEP 15: User Fill In Street Address Name (Line 3) Input ###############

streetaddressname_line3_input = driver.find_element(By.XPATH, "//input[@id='SH0B7PS']")
dummy_streetaddressname_line3 = "Et ipsam qui molesti"
streetaddressname_line3_input.send_keys(dummy_streetaddressname_line3)


########## STEP 16: User Fill In City Name Input ###############

cityname_input = driver.find_element(By.XPATH, "//input[@id='Q4W0FOB']")
dummy_cityname = "Error dolore culpa"
cityname_input.send_keys(dummy_cityname)


########## STEP 17: User Fill In State/Province Name Input ###############

stateprovincename_input = driver.find_element(By.XPATH, "//input[@id='BSAD4MN']")
dummy_stateprovincename = "Itaque quo officiis"
stateprovincename_input.send_keys(dummy_stateprovincename)


########## STEP 18: User Fill In Zip/Postal Code Input ###############

zippostalcode_input = driver.find_element(By.XPATH, "//input[@id='WES2UB9']")
dummy_zippostalcode = "faceheti@mailinator.com"
zippostalcode_input.send_keys(dummy_zippostalcode)


########## STEP 19: User Select Country  ###############

country_button = driver.find_element(By.XPATH, "//select[@id='JUF3S5C']")
country_button.click();


########## STEP 20: User Fill In Phone Number Input ###############

phonenumber_input = driver.find_element(By.XPATH, "//input[@id='W7VUH2H']")
dummy_phonenumber = "+1 (168) 329-2311"
phonenumber_input.send_keys(dummy_phonenumber)

########## STEP 21: User Select Shipping Method ###############

shippingmethod_button = driver.find_element(By.XPATH, "//input[@name='ko_unique_8']")
shippingmethod_button.click();

time.sleep(30)
