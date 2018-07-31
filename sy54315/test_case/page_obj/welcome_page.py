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
    edit_submit_successful_result_loc = (By.XPATH, '/html/body/div[1]/div[2]/p')
    # 旧密码框
    oldpwd_text_loc = (By.NAME, 'oldPwd')
    # 新密码框
    newpwd_text_loc = (By.NAME, 'newPwd')
    # 确认新密码框
    renewpwd_text_loc = (By.NAME, 'renewPwd')
    # 修改密码提交
    changepwd_submit_button_loc = (By.ID, 'Confirm')
    # 密码修改成功提示
    changepwd_successful_result_loc = (By.XPATH, '/html/body/div[1]/div[2]/p')

    # 进入编辑资料页面并提交修改资料
    def to_edit_myself_page(self):
        self.mouse_hover('XPATH', self.above)
        self.WaitElem('/html/body/header/ul/li[2]/p/a[1]')
        self.switch_to_window(1)
        self.find_element(*self.edit_myself_submit_button_loc).click()
        # sleep(1)
        # self.find_element(*self.edit_myself_button_loc).click()

    def submit_successful_result(self):
        return self.find_element(*self.edit_submit_successful_result_loc).text

    # 进入修改密码界面并修改密码
    def to_changepwd(self):
        self.mouse_hover('XPATH', self.above)
        self.WaitElem('/html/body/header/ul/li[2]/p/a[2]')
        self.switch_to_window(1)
        self.find_element(*self.oldpwd_text_loc).send_keys('qwe123')
        self.find_element(*self.newpwd_text_loc).send_keys('qwe123')
        self.find_element(*self.renewpwd_text_loc).send_keys('qwe123')
        self.find_element(*self.changepwd_submit_button_loc).click()

    def changepwd_successful_result(self):
        return self.find_element(*self.changepwd_successful_result_loc).text
