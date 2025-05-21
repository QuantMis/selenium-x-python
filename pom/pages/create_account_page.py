from selenium.webdriver.common.by import By

class CreateAccountPage:
    _INP_FIRSTNAME     = (By.ID, "firstname")
    _INP_LASTNAME      = (By.ID, "lastname")
    _INP_EMAIL         = (By.ID, "email_address")
    _INP_PASSWORD      = (By.ID, "password")
    _INP_PASSWORD_CONF = (By.ID, "password-confirmation")
    _BTN_CREATE        = (By.XPATH, "//button[@title='Create an Account']")

    def __init__(self, driver):
        self.driver = driver

    def register(
        self,
        first: str,
        last: str,
        email: str,
        password: str,
        confirm: str | None = None,
    ):
        """Fill the form and submit.  
        `confirm` defaults to the same value as `password`."""
        confirm = confirm or password
        d = self.driver
        d.find_element(*self._INP_FIRSTNAME).send_keys(first)
        d.find_element(*self._INP_LASTNAME).send_keys(last)
        d.find_element(*self._INP_EMAIL).send_keys(email)
        d.find_element(*self._INP_PASSWORD).send_keys(password)
        d.find_element(*self._INP_PASSWORD_CONF).send_keys(confirm)
        d.find_element(*self._BTN_CREATE).click()
        return self     

