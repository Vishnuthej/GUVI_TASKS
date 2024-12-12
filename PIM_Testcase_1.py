from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class PIM_module:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class Login(PIM_module):
    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#Method to Login to the OrangeHRM
    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)
        username = self.driver.find_element(by=By.NAME,value= "username").send_keys("admin")
        password = self.driver.find_element(by=By.NAME, value='password').send_keys("admin123")
        presslogin = self.driver.find_element(by=By.XPATH, value ="//button[@type ='submit']").click()
        sleep (5)
        return ("The user is logged in successfully")
    
#Method to add new employee details from PIM menu
    def add_employee(self):
        driver =self.driver
        pim_menu = driver.find_element(by= By.XPATH, value = "//a[@class ='oxd-text oxd-text--span oxd-main-menu-item--name' or @href='/web/index.php/pim/viewPimModule']").click()
        sleep (10)

        add_employee = driver.find_element(by = By.XPATH, value = "(//a[@class= 'oxd-topbar-body-nav-tab-item'])[2]")
        add_employee.click()
        sleep (10)
        firstname = driver.find_element(by = By.NAME, value = "firstName").send_keys("V")
        middlename = driver.find_element(by=By.NAME, value = "middleName").send_keys("T")
        lastname = driver.find_element(by= By.NAME, value = "lastName").send_keys("P8")
        save_info  = driver.find_element (by = By.XPATH, value = "//button[@type='submit']")
        save_info.click()

#Method to see a message for successful employee addition
    def successmsg(self):
        success_message_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By.XPATH, "//p[@class = 'oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"))
      
    # Retrieve and return the message text
        success_message = self.successmsg()
        return success_message


if __name__ == "__main__":
    pim = Login()
    print(pim.login())

    pim.add_employee()
    print("Employee details added successfully")
    
    print(pim.successmsg)
    sleep(5)

        
