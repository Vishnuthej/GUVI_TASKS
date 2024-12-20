import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests

def labour_task():
    # Initialize the WebDriver
    service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://labour.gov.in/")
    driver.maximize_window()

      # Hover over the "Documents" menu and click on the "Monthly Progress Report" link
    documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
    ActionChains(driver).move_to_element(documents_menu).perform()
    time.sleep(5)
    monthly_report = driver.find_element(By.XPATH, value="//a[@href='https://labour.gov.in/monthly-progress-report']").click()
    download_report = driver.find_element(By.XPATH, value="//a[@href='https://labour.gov.in/sites/default/files/mpr_september_2024.pdf']").click
     # Handle the confirmation dialog by accepting it (clicking "OK")
    try:
        alert = driver.switch_to.alert
        alert.accept()  # Clicks "OK"
    except:
        print("No alert found")

    # Wait for download to complete
    time.sleep(10)  

    
      # Define download directory
    download_dir = "photo_gallery"
    # Go to "Media" -> "Photo Gallery" and download 10 photos
    media_menu = driver.find_element(By.LINK_TEXT, "Media")
    ActionChains(driver).move_to_element(media_menu).perform()

    photo_gallery = driver.find_element(By.LINK_TEXT, "Photo Gallery")
    photo_gallery.click()

    # Create directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    images = driver.find_elements(By.XPATH, "//div[@class='views-field views-field-field-image']//img")
    for i, img in enumerate(images[:10]):
        img_url = img.get_attribute("src")
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(f"{download_dir}/photo_{i + 1}.jpg", "wb") as file:
                file.write(response.content)

    driver.quit()

if __name__ == "__main__":
    labour_task()
