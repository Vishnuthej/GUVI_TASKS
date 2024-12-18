from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HRM_Login:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class login(HRM_Login):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # To start the browser window and maximize it
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)

 # Method to Login with username and password locators
    def login_page(self):
        self.driver.find_element(by=By.NAME, value="username").send_keys("admin")
        self.driver.find_element(by=By.NAME, value="password").send_keys("admin123")
        self.driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        sleep(5)
        return "The user is logged in successfully"

 # Method to validate the page title
    def validate_title(self, expected_title):
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Expected title to be {expected_title}, but got {actual_title}"
        return f"Page title '{actual_title}' validated successfully"

    # Method to validate menu items in the ADMIN page
    def validate_admin_Mainmenu_items(self):
        driver = self.driver
        admin_menu = driver.find_element(by=By.XPATH, value="//a[@href='/web/index.php/admin/viewAdminModule']").click()
        sleep(3)
        # Creating a Dictionary to store all the targetted web elements & their Xpaths (locators)
        Mainmenu_items ={
            "a) Admin": "//a[@href='/web/index.php/admin/viewAdminModule']",
            "b) PIM": "//a[@href='/web/index.php/pim/viewPimModule']",
            "c) Leave": "//a[@href='/web/index.php/leave/viewLeaveModule']",
            "d) Time": "//a[@href='/web/index.php/time/viewTimeModule']",
            "e) Recruitment": "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']",
            "f) My Info": "//a[@href='/web/index.php/pim/viewMyDetails']",
            "g) Performnace": "//a[@href='/web/index.php/performance/viewPerformanceModule']",
            "h) Dashboard" : "//a[@href='/web/index.php/dashboard/index']",
            "i) Directory": "//a[@href='/web/index.php/directory/viewDirectory']",
            "j) Maintenance": "//a[@href='/web/index.php/maintenance/viewMaintenanceModule']",
            "k) Buzz": "//a[@href='/web/index.php/buzz/viewBuzz']"
            }

        for item_name, item_xpath in Mainmenu_items.items():
            try:
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, item_xpath)))
                print("Mainmenu item"+" "+item_name+" "+"is visible")
            except TimeoutException:
                print(f"Mainmenu item '{item_name}' is NOT visible")

if __name__ == "__main__":
    user_login = login()
    user_login.start()
    
    # Test case 1: LOGIN SUCCESS 
    print(user_login.login_page())
    
    # Validate the page title after logging in
    print(user_login.validate_title("OrangeHRM"))
    
    # Validate the menu items in the ADMIN page
    user_login.validate_admin_Mainmenu_items()
    
    sleep(5)
    user_login.driver.quit()
