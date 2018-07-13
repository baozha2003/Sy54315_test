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
    # 编辑提交个人资料
    edit_myself_submit_button_loc = (By.ID, 'Confirm')
    # 提交资料成功提示
    edit_submit_successful_result = (By.XPATH, '/html/body/div[1]/div[2]/p')

    def to_edit_myself_page(self):
        self.mouse_hover('XPATH', self.above)
        self.WaitElem('/html/body/header/ul/li[2]/p/a[1]')
        self.switch_to_window(1)
        self.find_element(*self.edit_myself_submit_button_loc).click()
        # sleep(1)
        # self.find_element(*self.edit_myself_button_loc).click()

    def submit_successful_result(self):
        return self.find_element(*self.edit_submit_successful_result).text
