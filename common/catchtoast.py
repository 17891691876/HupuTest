from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class getToast():
    def get_toast(driver, text, timeout=5, poll_frequency=0.5):
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        toastS = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        message = toastS.text
        return message