from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://jqueryui.com/droppable/"
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(5)

# Wait for the iframe to be available and switch to it
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

# Wait for the draggable and droppable elements to be visible
small_draggable_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "draggable")))
big_droppable_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "droppable")))

def drag_drop_box():
    small_draggable_box = driver.find_element(By.ID, value="draggable")
    big_droppable_box = driver.find_element(By.ID, value="droppable")
    # Actions class to perform drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(small_draggable_box, big_droppable_box).perform()
    # waiting time to see the output 
    time.sleep(2)
    # Taking screenshot of the recent action saving to a location and give a name to the image
    driver.get_screenshot_as_file("E:/GUVI Material/Python Programs/DAY_23_TASK-11/dropped_rectangle.png")
if __name__ == "__main__":
    drag_drop_box()