from common.common_fun import Common,By
from common.desired_caps import appium_desired
from businessView.mygoldPage import mygold
class mytab(Common):
    jd_num = (By.ID, "com.hupu.games:id/gold_num")
    hupu_coin = (By.ID,"com.hupu.games:id/hupucoin_num")
    def click_jd_num(self):
        self.find_element(mytab.jd_num).click()
        return mygold(self.driver)