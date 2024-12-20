from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def display_cookies():
        # Set up the WebDriver 
    service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# Initialize the Chrome WebDriver with the Service object
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Display cookies before login
    print("Cookies before login:")
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)
        #print(type(cookie))

    # Perform login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for login to complete
    time.sleep(5)

    # Display cookies after login
    print("\nCookies after login:")
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)
# Perform logout
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()

 # Close the browser
    driver.quit()

if __name__ == "__main__":
    display_cookies()
