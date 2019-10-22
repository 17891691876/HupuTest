import logging
from common.common_fun import Common,By
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import time
class LoginView(Common):
    usermore = (By.ID,"com.hupu.games:id/btn_mytab")
    login_button = (By.ID,"com.hupu.games:id/bt_quick_other")
    mobile_login_new =(By.ID,"com.hupu.games:id/mobile_login_new")
    acount_login = (By.ID,"com.hupu.games:id/bt_accout_login")
    username_type = (By.ID,"com.hupu.games:id/username_text")
    password_type = (By.ID,"com.hupu.games:id/password_text")
    login_submit = (By.ID,"com.hupu.games:id/bt_submit")
    def login_action(self,username,password):
        logging.info(">>>>>>>>start login<<<<<<<<<")
        time.sleep(5)
        self.driver.find_element(*self.usermore).click()
        try:
            self.driver.find_element(*self.mobile_login_new).click()
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.login_button).click()

        self.driver.find_element(*self.mobile_login_new).click()
        self.driver.find_element(*self.acount_login).click()
        #self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.username_type).send_keys(username)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.login_submit).click()
if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('17891691876','fuyangdi123')


