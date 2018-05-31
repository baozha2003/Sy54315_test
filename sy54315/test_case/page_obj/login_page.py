from selenium.webdriver.common.by import By
from .base import Base


class LoginPage(Base):
    url = '/'
    login_username_text_loc = (By.NAME, 'mobile')
    login_password_text_loc = (By.NAME, 'password')
    login_button_loc = (By.ID, 'login')
    login_error_hint_loc = (By.XPATH,'/html/body/section/div/form/ul/li[3]')

    # 把每一个元素封装成一个方法
    def login_username(self, text):
        self.find_element(*self.login_username_text_loc).send_keys(text)

    def login_password(self, text):
        self.find_element(*self.login_password_text_loc).send_keys(text)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    def login_action(self, username, password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()
