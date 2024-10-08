"""Using Python selenium Automation and the URL https://www.instagram.com/guviofficial/ kindly do the following mentioned tasks:

1) Use either Relative or Absolute XPATH only for the task.

2) Extract the total number of Followers andFollowing from the URL mentioned above"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class guvi_insta_profile:
    url = "https://www.instagram.com/guviofficial/"
    
    
class followers(guvi_insta_profile):
    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    
    def start(self):
       self.driver.maximize_window()
       self.driver.get(self.url)
       sleep(10)
    
    
    def followers_count(self):
       followers = self.driver.find_elements(by=By.XPATH, value='//button[text()=" followers"]')
       return len(followers)

    def following_count(self):
       following_number = self.driver.find_elements(by=By.XPATH, value='//button[text()=" following"]')
       return len(following_number)


if __name__ == "__main__":
   Instagram = followers()
   Instagram.start()
   print(Instagram.followers_count())
   print(Instagram.following_count())
   Instagram.shutdown()
