from common.myunit import StartEnd
import logging
from businessView.mygoldPage import mygold
from businessView.navigationPage import navigation_button
from businessView.mytabPage import mytab
import unittest
#@unittest.skip
class mygoldCase(StartEnd,unittest.TestCase):

    jd_num = mytab.jd_num

    #@unittest.skip
    def test_buyGoldtest(self):

        # 点击更多，跳转到我的页面
        navigation_button2 = navigation_button(self.driver)
        newmytab = navigation_button2.click_btn_mytab()
        #点击金豆按钮到金豆页面
        newmygoldPage = newmytab.click_jd_num()
        #购买金豆余额充足
        num = 1
        newmygoldPage.buy_gold(num)
        gold_details = newmygoldPage.getFirstDetail()
        self.assertEquals("购买金豆", gold_details[0])
        self.assertEquals("+"+str(num), gold_details[1])
        #查看跳转列表是否正确
        guessRank = newmygoldPage.getGuessRank()
        self.assertEquals("竞猜排行",guessRank)
        guessRecord = newmygoldPage.getGuessRecord()
        self.assertEquals("竞猜记录", guessRecord)
        goldMarket = newmygoldPage.getGoldMarket()
        self.assertEquals("金豆商城", goldMarket)


if __name__ == '__main__':
    unittest.main()
