from selenium.webdriver.common.by import By

class HomePage():
    # variable (locators)
    create_account_hyperlink=(By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    sign_in_hyperlink=(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
    minicart_hyperlink = (By.XPATH, "//a[@class='action showcart']"
    searchbar = (By.XPATH, "//input[@id='search']"
    whatsnew_hyperlink = (By.XPATH, "//a[@id='ui-id-3']//span[1]")
    homebanner_img = (By.XPATH, "//img[@src='https://magento.softwaretestingboard.com/pub/media/wysiwyg/home/home-main.jpg']")
