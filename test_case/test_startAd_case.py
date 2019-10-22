from common.myunit import StartEnd
import logging
from businessView.startPage import start_ad
from businessView.navigationPage import navigation_button
import unittest
class startAdCase(StartEnd,unittest.TestCase):

    def test_isexist_ad(self):
        start_ad2 = start_ad(self.driver)

        #应该有广告时
        self.assertTrue(start_ad2.check_ad_isexist())

        # 应该没有广告时
        #self.assertFalse(start_ad2.check_ad_isexist())



    def test_clickSkip(self):
        start_ad2 = start_ad(self.driver)
        navigation_button2 = start_ad2.check_adSkip()

        if navigation_button2 is False :
            logging.info("跳过失败了")

        else:
            self.assertTrue(navigation_button2.isExistnews_button())




if __name__ == '__main__':
    unittest.main()


