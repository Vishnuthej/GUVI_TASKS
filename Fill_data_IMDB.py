from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search_imdb():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/search/name/")
    driver.maximize_window()

    try:
        # Scroll down the page
        driver.execute_script("window.scrollTo(0, 600);")

        # Wait for the input box to be visible and locate the element
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@class = 'ipc-tab ipc-tab--on-base ipc-tab--active']"))
        )
        
        # Click on the desired name element
        driver.find_element(By.XPATH, value="(//span[@class = 'ipc-accordion__item__title'] | //div[@class = 'sc-6addea7c-0 jfSEAR']) [1]").click()
        
        # Enter text in the name text box
        driver.find_element(By.XPATH, value="//input[@aria-label = 'Name']").send_keys("James Stewart")

        # Gender of the celeb person
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "accordion-item-genderIdentityAccordion"))
        )
         # Scroll down the page
        driver.execute_script("window.scrollTo(0, 300);", element)
        element.click()
        
        # Select gender as male
        driver.find_element(By.XPATH,value = "//button[@data-testid='test-chip-id-MALE']").click()

        # Click on the See results button
        driver.find_element(By.XPATH, value = "//button[@class = 'ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-accent1 ipc-btn--theme-base ipc-btn--button-radius sc-13add9d7-4 cwcOrs']").click()
        
        # Wait for a movie to appear
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/title/tt0052561/?ref_=sr_knf_1']"))
        )


    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    search_imdb()
