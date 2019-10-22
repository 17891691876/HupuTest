
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import logging
class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        try:
            elm = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(*loc))
            return elm
        except NoSuchElementException:
            logging.error("*********元素没找到*********")
        except TimeoutException:
            logging.error("*********元素没找到*********")


    def find_elements(self,*loc):
        try:
            elms = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(*loc))
            return elms
        except NoSuchElementException:
            logging.error("*********元素没找到*********")
        except TimeoutException:
            logging.error("*********元素没找到*********")

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,star_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(self,star_x,start_y,end_x,end_y,duration)





