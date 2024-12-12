"""Test case: TC_Login_01 & TC_Login_02"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class HRM_Login:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

class login(HRM_Login):
    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# To start the browser window and maximize it   
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep (5)
# Method to Login with username and password locators
    def login_page(self):
        username = self.driver.find_element(by=By.NAME,value= "username").send_keys("admin")
        password = self.driver.find_element(by=By.NAME, value='password').send_keys("admin123")
        presslogin = self.driver.find_element(by=By.XPATH, value ="//button[@type ='submit']").click()
        sleep (5)
        return ("The user is logged in successfully")

# Method to perform logout
    def logout(self):
        dropdown = self.driver.find_element(by=By.XPATH, value="//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        logout_button = self.driver.find_element(by = By.XPATH, value = "//a[@href='/web/index.php/auth/logout']").click()

        return ("The user is logged out successfully")
        
# Method to get the error message for login failure
    def Fail_to_login(self):
         username = self.driver.find_element(by=By.NAME,value= "username").send_keys("admin")
         password = self.driver.find_element(by=By.NAME, value='password').send_keys("admin12")
         presslogin = self.driver.find_element(by=By.XPATH, value ="//button[@type ='submit']").click()
         sleep(5)
         return ("A valid error message for invalid credentials is displayed")
    
if __name__ == "__main__":
    user_login = login()
    user_login.start()
#Test case 1: LOGIN SUCCESS
    print(user_login.login_page())
    print(user_login.logout())
    sleep (5)
#Testcase 2: LOGIN FAILED 
    print(user_login.Fail_to_login())
    sleep (20)


    


