from selenium.webdriver.common.by import By
from .base import Base
from time import sleep


class WelcomePage(Base):
    # 编辑个人资料页面
    edit_myself_button_loc = (By.XPATH, '/html/body/header/ul/li[2]/p/a[1]')
    # 修改密码页面
    changepwd_button_loc = (By.XPATH, '/html/body/header/ul/li[2]/p/a[2]')
    # 鼠标悬停姓名处
    above = "/html/body/header/ul/li[2]/i[1]"

    def to_edit_myself_page(self):
        self.mouse_hover(self.above)
        self.WaitElem(self.driver, xpath='/html/body/header/ul/li[2]/p/a[1]', timeout=5).click()
        # sleep(1)
        # self.find_element(*self.edit_myself_button_loc).click()
