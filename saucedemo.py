from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up the WebDriver 
service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=service)
try:
    # Step 1: Open the webpage
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)  # Wait for the page to load
    
    # Step 2: Log in with provided credentials
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    time.sleep(2)  # Wait for the login to complete
    
    # Step 3: Fetch the title of the webpage
    title = driver.title
    print(f"Title of the webpage: {title}")
    
    # Step 4: Fetch the current URL of the webpage
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    
    # Step 5: Extract the contents of the webpage
    page_source = driver.page_source
    
    # Save the content to a text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_source)
    print("Webpage content saved in 'Webpage_task_11.txt'.")
    
finally:
    # Close the WebDriver
    driver.quit()
