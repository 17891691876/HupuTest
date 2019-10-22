import logging
from common.common_fun import Common,By
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from common.catchtoast import getToast
import time
class mygold(Common):
    buy_button = (By.ID,"com.hupu.games:id/txt_pay")  #购买按钮
    gold_num = (By.ID,"com.hupu.games:id/txt_coin_num")  #金豆值元素
    back_button = (By.ID,"com.hupu.games:id/btn_back")   #返回按钮
    detail = (By.ID,"com.hupu.games:id/txt_coin_info")  #明细
    guessrank = (By.ID,"com.hupu.games:id/menu_rank_info")  #竞猜排行
    guessrecord = (By.ID,"com.hupu.games:id/layout_guess_result")  #竞猜记录
    goldmarket = (By.ID,"com.hupu.games:id/coin_prize")  #商城

    #购买页元素
    hupucoin_num = (By.ID,"com.hupu.games:id/txt_kanqiu_money")  #虎扑币的值
    buy_Jd_num = (By.ID,"com.hupu.games:id/txt_wallet")  #购买金豆值
    buy_submit = (By.ID,"com.hupu.games:id/btn_exchange")   #购买提交按钮
    ask_buy_ok = (By.ID,"com.hupu.games:id/right_btn")  #询问是否购买


    #明细页面
    gold_detail = (By.ID,"com.hupu.games:id/text_guess_result")
    detail_list_name = (By.XPATH,"//android.widget.ListView[@resource-id = 'detail-list']/android.view.View[1]/android.view.View")
    back_gold_button = (By.ID,"com.hupu.games:id/btn_back_arrow")

    intitle = (By.ID, "com.hupu.games:id/txt_title")  # 竞猜排行  竞猜记录  商城


    #购买金豆
    def buy_gold(self,by_Jdnum):
        logging.info(">>>>>>>start buy gold<<<<<<<<<<<")
        self.find_element(mygold.buy_button).click()
        self.find_element(mygold.buy_Jd_num).send_keys(by_Jdnum)
        self.find_element(mygold.buy_submit).click()
        ask_message = self.driver.find_element(mygold.ask_buy_ok).click()

        #获取toast信息
        successtoast = getToast.get_toast(self.driver,"成功购买1个金豆")
        logging.info(successtoast)
        self.find_element(mygold.back_button).click()
        return successtoast

    #获取金豆明细的第1条记录
    def getFirstDetail(self):
        self.find_element(mygold.detail).click()
        self.find_element(mygold.gold_detail).click()
        detailfirst = self.find_elements(mygold.detail_list_name)  #.find_elements(mygold.detail_list_name)[0]
        # for i in detailfirst:
        #     print(i.text)
        # print("+++++++++++++++++++3",detailfirst[1].text)      #这种方式也可以
        self.find_element(mygold.back_gold_button).click()
        self.find_element(mygold.back_button).click()
        return detailfirst

    #返回竞猜排行页面标题
    def getGuessRank(self):
        self.find_element(mygold.guessrank).click()
        guessrankTitlein =self.find_element(mygold.guessrankin).text
        self.find_element(mygold.back_button).click()
        return guessrankTitlein

    #返回竞猜记录页面标题
    def getGuessRecord(self):
        self.find_element(mygold.guessrecord).click()
        guessrecordTitlein =self.find_element(mygold.guessrecordin).text
        self.find_element(mygold.back_button).click()
        return guessrecordTitlein

    #返回金豆商城页面标题
    def getGoldMarket(self):
        self.find_element(mygold.goldmarket).click()
        goldMarket =self.find_element(mygold.goldmarketin).text
        self.find_element(mygold.back_button).click()
        return goldMarket


if __name__ == "__main__":
    driver = appium_desired()
    a = mygold(driver)
    a.getFirstDetail()