#Importing required libraries
from PIM_Testcase_1 import Login
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

#Creating a class to edit the employee details from the existing list of employees
class edit_employee:
    
    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
#A Method to search the employee by "employeeID"
    def search_existing_employee(self,employee_id):
        try:
            driver = self.driver
        # Click on the PIM menu
            pim_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']")) )
            pim_menu.click()
            print("Clicked on PIM menu.")

        # Wait for the employee ID input to be visible
            employee_id_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active'][2]")))
            employee_id_input.send_keys(employee_id)

        # Click the search button
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            search_button.click()
            print("Searching for employee details.")

            return True  # Indicate success

        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # Indicate failure
# To update the employee details we need to click on the "edit" button        
    def edit_emp_details(self):
        driver = self.driver
        self.edit_icon = None
        while not self.edit_icon:
            try:
                self.edit_icon = WebDriverWait(self.driver, 5).until(EC.element_to_be_visible(by= By.XPATH, value = "//i[@class='oxd-icon bi-pencil-fill']")).click()
                self.actions = ActionChains (self.driver)
                # Scrolling the page until the target element to be visible using actions class 
                self.actions.scroll_to_element(self.edit_icon)
               
            except NoSuchElementException:
                self.driver.execute_script("window.scrollBy(0,500);",self.edit_icon)
            return ("Now, you can edit/add the employee details ")

# A method to add the multiple details of the employee
    def add_details(self):
        driver = self.driver
        add_middle_name = driver.find_element(by= By.XPATH, value = "//input[@name = 'middleName' and @placeholder = 'Middle Name']").send_keys("Thej")
        other_id = driver.find_element(by=By.XPATH, value= "//input[@class='oxd-input oxd-input--active' and @fdprocessedid='a80mr4']").send_keys("7212_aadhar")
        gender = driver.find_element(by= By.XPATH, value= "//input[@type = 'radio' and @value = '2']").click()
        save_button = driver.find_element(by= By.XPATH, value= "//button[@type = 'submit' and @class = 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space' and @fdprocessedid = 'q0xki']").click()
        return ("Successfully added the details of employee")
# Main method to create references to the class and imported class to call all the methods
if __name__ == "__main__":
# Creating reference to the imported class to utilize the required methods 
    login_emp = Login()
    print(login_emp.login())

# Reference to the present class edit employee
    emp_list = edit_employee()
    print(emp_list.search_existing_employee("0476"))
    sleep(5)
    print(emp_list.edit_emp_details())
    print(emp_list.add_details())




    

    



