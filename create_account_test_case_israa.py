# import selenium package to use automation class
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# STEP 1: Open Browser
driver = webdriver.Chrome()

# STEP 2: Open Magento
driver.get("https://magento.softwaretestingboard.com/")

# STEP 3: Click Create Account hyperlink
# Detail: 1) Locate the element using selenium
#         2) Click the element using selenium

# bagi criteria element dekat selenium, supaya dia boleh cari
# 1) Kita cari element <a>
# 2) Kita dapat banyak element <a>
# 3) Kita pilih element <a> yang kedua sebab itu yang kita nak
# 4) Kita click element yg kita pilih tu
test = driver.find_elements(By.TAG_NAME, "a")
test[2].click()
