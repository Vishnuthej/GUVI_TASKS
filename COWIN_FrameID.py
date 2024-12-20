from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

def cowin_task():
    # Initialize the WebDriver
    service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)  
    driver.get("https://www.cowin.gov.in/")

    # Click on the "Create FAQ" and "Partners" anchor tags to open new windows
    faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
    partners_link = driver.find_element(By.LINK_TEXT, "PARTNERS")

    faq_link.send_keys(Keys.CONTROL + Keys.RETURN)  # Open in new window
    partners_link.send_keys(Keys.CONTROL + Keys.RETURN)  # Open in new window

    # Switch to the new windows and print their handles
    windows = driver.window_handles
    print("Opened Windows/Frame IDs:")
    for window in windows:
        print(window)

    # Close the new windows and switch back to the main window
    for window in windows[1:]:
        driver.switch_to.window(window)
        driver.close()

    driver.switch_to.window(windows[0])
    driver.quit()

if __name__ == "__main__":
    cowin_task()


OUTPUT:
Opened Windows/Frame IDs:
1347CEC384DC4CC8D51A5B3B79A5A5D4
B6B8A4837F05B1C05EF1BB53BEDBE3B6
E6E72D57B1707294B33CE0963AB52C4A
