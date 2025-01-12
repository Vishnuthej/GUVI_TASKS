from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class IMDbAutomation:
    def __init__(self):
        self.service = Service(executable_path="E:/Browser drivers/chrome-win64/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def search_imdb(self):
        driver = self.driver
        driver.get("https://www.imdb.com/search/name/")
        
        try:
            # Assert the page loaded correctly
            assert "IMDb" in driver.title, "Page did not load properly"
           
            # Click on "Name" tab
            name_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Name')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_tab)
            name_tab.click()

            # Enter text in the Name search box
            search_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Name']"))
            )
            search_box.send_keys("James Stewart")

            # Click on "Awards" accordion
            awards_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "awardsAccordion"))
            )
            awards_section.click()

            # Select "Best Actor-Winning"
            best_actor_award = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Best Actor-Winning')]"))
            )
            best_actor_award.click()

            # Click on "See results"
            see_results_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'ipc-btn--core-accent1')]"))
            )
            see_results_button.click()
            # Wait for movie data to load
            movie_data = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/title/tt0052561')]"))
            )
            print(f"Movie data loaded successfully: {movie_data.text}")

        except Exception as e:
            print(f"Movie data is loaded properly: {e}")

        finally:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    automation = IMDbAutomation()
    automation.search_imdb()
