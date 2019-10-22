from common.common_fun import Common,By
from businessView.mytabPage import mytab
class navigation_button(Common):
    news_button = (By.ID,"com.hupu.games:id/btn_news")
    game_button = (By.ID,"com.hupu.games:id/btn_game")
    bbs_button = (By.ID,"com.hupu.games:id/btn_bbs")
    data_button = (By.ID,"com.hupu.games:id/btn_data")
    btn_mytab = (By.ID,"com.hupu.games:id/btn_mytab")

    #判断是否存在更多页面
    def isExistnews_button(self):
        return self.isExistElement(navigation_button.news_button)

    def click_btn_mytab(self):
        self.find_element(navigation_button.btn_mytab).click()
        return mytab(self.driver)

