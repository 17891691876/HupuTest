import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======setUp=========')
        self.driver=appium_desired()

        #自动跳过广告，如果是测试开机广告需要注释
        #sleep(8)



    def tearDown(self):
        sleep(10)
        logging.info('======tearDown=====')
        self.driver.close_app()

