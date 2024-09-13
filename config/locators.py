from selenium.webdriver.common.by import By


class HomePageLocators:
    GO_TO_LOGIN_BTN = (By.CSS_SELECTOR, 'a.sc-fQpRED:nth-child(5)')
    GO_TO_REGISTER_BTN = (By.CSS_SELECTOR, 'a.sc-fQpRED:nth-child(3)')

class LoginPageLocators:
    LOGIN_TITLE = (By.TAG_NAME, "h2")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BTN = (By.XPATH, "/html/body/div/div/form/button")

class RegisterPageLocators:
    REGISTER_TITLE = (By.TAG_NAME, "h2")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//div[2]/input")
    CONFIRM_PASSWORD = (By.XPATH, "//div[3]/input")
    REGISTER_BTN = (By.XPATH, "//button[@type='submit']")

class DashboardPageLocators:
    FEEDBACK_FIELD = (By.ID, "feedback")
    SUBMIT_FEEDBACK_BTN = (By.XPATH, "//button[@type='submit']")
