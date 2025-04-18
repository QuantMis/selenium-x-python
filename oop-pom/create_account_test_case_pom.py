from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CreateUserAccountPage:

    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    userInput = (By.ID, "firstname")
    lastInput = (By.ID, "lastname")

    def fillInput(input, value):
        pass

    def clickSubmitButton():
        pass

if __name__ == "__main__":
    createUserPage = CreateUserAccountPage()
    createUserPage.fillInput(userInput, "nur-alia")
    createUserPage.fillInput(lastInput, "nur-alia")
    createUserPage.clickSubmitButton()

