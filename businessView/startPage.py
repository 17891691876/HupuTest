from common.common_fun import Common,By
from selenium.common.exceptions import NoSuchElementException
from businessView.navigationPage import navigation_button
import logging
class start_ad (Common):
    # 头条广告其余广告自行获取
    #ad = (By.ID,"com.hupu.games:id/tt_splash_ad_gif")
    #ad = (By.ID,"com.hupu.games:id/img_ads_full")
    ad = (By.ID,"com.hupu.games:id/surfaceView")


    adSkip = (By.ID,"com.hupu.games:id/ll_timer_jump")

    # 查询是否存在开机广告
    def check_ad_isexist(self):
        logging.info("开始查找是否存在广告")
        ad_boolean =self.isExistElement(start_ad.ad)
        print("111111111",ad_boolean)
        return ad_boolean


    # 跳过开机广告到首页中
    def check_adSkip(self):
        isexistAD = self.check_ad_isexist()

        if isexistAD is True:
            logging.info("查找是否存在跳过按钮")
            isexistSkip = self.isExistElement(start_ad.adSkip)

            if isexistSkip:
                self.find_element(start_ad.adSkip).click()

                return navigation_button(self.driver)

            else:
                logging(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>no skip button")
                return False
        else:
            logging(">>>>>>>>>>>>>>>>>>>>>>>>>>>no ad need't skip")
            return False
        return True

