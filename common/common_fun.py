import logging
import logging.config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
import time
import os
import csv


class Common(BaseView):


    #获取屏幕尺寸
    def get_screenSize(self):
        x = self.get_window_size()["width"]
        y = self.get_window_size()["height"]
        return (x,y)

    #左滑
    def swipeLeft(self):
        logging.info("swipeLeft")
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1,y1,x2,y1,1000)

     #类似时间戳
    def get_Time(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    #获取截图
    def getScreenShot(self,module):
        time = self.get_Time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/%s_%s.png" % (module,time)
        logging.info("get %s screenshot" %module)
        self.driver.get_screenshot_as_file(image_file)




    #获取csv文件指定行的数据
    def get_csv_data(self,csv_file,line):
        with open(csv_file,"r",encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            #1指的是索引起始值从1开始，也就是index从1开始，把第一行当做1而不是0
            for index,row in enumerate(reader,1):
                if index == line:
                    return row

    #检测是否存在某个元素
    def isExistElement(self, elms):
        try:

            elm = self.find_element(elms)
        except NoSuchElementException:
            return False
        else:
            return True

if __name__ =="__main__":
     driver = appium_desired()
    # a = Common(driver)
    # a.isExistElement()






















