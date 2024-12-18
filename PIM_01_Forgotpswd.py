from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class HRM_Login:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class forgot_pswd(HRM_Login):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 # To start the browser window and maximize it   
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        return "Browser started and maximized successfully"

# Method to Login with username and password locators
    def login_page(self):
        driver = self.driver
        driver.find_element(by=By.NAME, value="username").send_keys("admin")
        driver.find_element(by=By.XPATH, value="//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
        sleep(5)
        print("Reset password window opened successfully")
        driver.find_element(by=By.NAME, value="username").send_keys("admin")
        driver.find_element(by=By.XPATH, value="//button[@class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']").click()

# Method to see a message for reset password
    def successmsg(self):
        try:
# Wait for the element to be visible
            success_message_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"))
            )
# Retrieve and return the message text
            success_message = success_message_element.text
            return success_message
        except TimeoutException:
            raise ElementNotFoundException("The success message element was not found within the given time.")

class ElementNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

if __name__ == "__main__":
    user_login = forgot_pswd()
    print(user_login.start())
    user_login.login_page()
    try:
        print(user_login.successmsg())
    except ElementNotFoundException as e:
        print(e)
    sleep(5)
    user_login.driver.quit()
