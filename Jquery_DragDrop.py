from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Class with url and screenshot path
class UrlAndScreenshot:
    url = "https://jqueryui.com/droppable/"
    screenshot_path = "E:/GUVI Material/Python Programs/DAY_23_TASK-11/dropped_rectangle.png"

# class with actual logic and taking the above class as parameter
class DragAndDrop(UrlAndScreenshot):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def open_page(self):
    #Method to open the target url and page  
        self.driver.get(self.url)
        # Switch to the iframe containing the draggable and droppable elements
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame"))
        ) 
        # explicit wait for the targetted frame

    def perform_drag_and_drop(self):
       
        try:
            # Locate draggable and droppable elements
            small_draggable_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "draggable"))
            )
            big_droppable_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "droppable"))
            )

            # Perform drag and drop using ActionChains
            actions = ActionChains(self.driver)
            actions.drag_and_drop(small_draggable_box, big_droppable_box).perform()

            # Explicit wait to ensure the action has completed (check for the drop effect)
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!")
            )

            # Take a screenshot and save it
            self.driver.get_screenshot_as_file(self.screenshot_path)
        
        # Exception raising to handle the error 
        except Exception as e:
            print(f"Error during drag-and-drop: {e}")

    def close_browser(self):
        """Close the browser session."""
        self.driver.quit()

if __name__ == "__main__":
    # Create an instance of the DragAndDrop class
    test = DragAndDrop()
    
    # Calling all the methods
    try:
        test.open_page()
        test.perform_drag_and_drop()
    finally:
        test.close_browser()
