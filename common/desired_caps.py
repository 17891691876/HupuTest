from appium import webdriver
import yaml
import logging
import logging.config
import os
from selenium.webdriver.support import expected_conditions as EC

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    print("111111111")
    with open("../config/hupu_caps.yaml","r",encoding="utf-8") as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    #真机的时候使用
    #desired_caps["udid"] = data["udid"]

    base_dir = os.path.dirname(os.path.dirname(__file__)) #common的绝对路径
    #app_path = os.path.join(base_dir,"app",data["appname"])
    #desired_caps["app"] = app_path  #只需要更换包就可以了路径自动生成

    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] =data["appActivity"]
    desired_caps["noReset"] = data["noReset"]
    desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
    desired_caps["resetKeyboard"] =data["resetKeyboard"]
    desired_caps["automationName"] =data["automationName"]

    logging.info(">>>>>>>start app<<<<<<<")
    driver = webdriver.Remote("http://"+str(data["ip"]+":"+str(data["port"])+"/wd/hub"),desired_caps)
    driver.implicitly_wait(4)

    #driver.find_elements().
    return driver
if __name__ == "__main__":
    appium_desired()
