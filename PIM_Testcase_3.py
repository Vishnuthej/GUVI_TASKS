from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# Reusing the code by importing the required classes
from PIM_Testcase_1 import Login
from PIM_Testcase_2 import edit_employee


class delete_employee:
    def __init__(self):
        self.driver = WebDriver.chrome(service = Service(ChromeDriverManager().install()))
# A method to perform the delete action on the existing employee
    def delete_employee_details(self):
        driver = self.driver
        self.delete_icon = None
        while not self.delete_icon:
            try:
                self.delete_icon = WebDriverWait(self.driver, 5).until(EC.element_to_be_visible(by= By.XPATH, value = "//i[@class= 'oxd-icon bi-trash']")).click()
                self.actions = ActionChains (self.driver)
                # Scrolling the page until the target element to be visible using actions class 
                self.actions.scroll_to_element(self.edit_icon)
                accept_delete_button = driver.find_element(by=By.XPATH, value = "//i[@class= 'oxd-icon bi-trash oxd-button-icon']").click()
            except NoSuchElementException:
                self.driver.execute_script("window.scrollBy(0,500);",self.edit_icon)
            return ("Permanently deleted the employee details")
# Main method to create references to the class and imported class to call all the methods        
if __name__ == "__main__":
# Reference to the login class--Login_Testcase_1_2
    emp_login = Login()
    print(emp_login.login())
# Reference to the edit_employee class--PIM_Testcase_2
    existing_employee = edit_employee()
    print(existing_employee.search_existing_employee("0476"))
# Reference to the present class
    delete = delete_employee()
    print(delete.delete_employee_details())
