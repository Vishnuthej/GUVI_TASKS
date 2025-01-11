from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class path_for_saucedemo():
    url = "https://www.saucedemo.com/"
      # Set up the WebDriver 
    service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
class Saucedemo(path_for_saucedemo):
    try: 
        def __init__(self):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.maximize_window()

        def display_cookies(self):  
            # Initialize the Chrome WebDriver with the Service object
            self.driver.get(self.url)        

            # Display cookies before login
            print("Cookies before login:")
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                print(cookie)
                #print(type(cookie))

            # Perform login
            username_field = self.driver.find_element(By.ID, "user-name")
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            username_field.send_keys("standard_user")
            password_field.send_keys("secret_sauce")
            login_button.click()

            # Wait for login to complete
            WebDriverWait(self.driver, 10).until (EC.visibility_of_element_located((By.ID,"react-burger-menu-btn")))

            # Display cookies after login
            print("\nCookies after login:")
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                print(cookie)
           
            # Perform logout
            menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
            menu_button.click()
            logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
            logout_link.click()
    except Exception as e:
        print(f"Menu item is not visible :{e}")
    
    # Method to close the browser
    def close_browser(self):
       
        self.driver.quit()

if __name__ == "__main__":
    # Instance of the class and calling the methods
    demo = Saucedemo()
    demo.display_cookies()
    demo.close_browser()
