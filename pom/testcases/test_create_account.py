from selenium import webdriver
from pom.pages.create_account_page import CreateAccountPage 

def test_can_register_new_user():
    driver = webdriver.Chrome()
    try:
        (CreateAccountPage(driver)
            .register(
                first="nur",
                last="alia",
                email="test@gmail.com",
                password="Abc12345def",
            )
        )
    finally:
        driver.quit()

if __name__ == "__main__":
    test_can_register_new_user()
