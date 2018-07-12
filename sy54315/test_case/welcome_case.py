from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.welcome_page import WelcomePage
from sy54315.test_case.page_obj.login_page import LoginPage

sys.path.append('./models')
sys.path.append('./page_obj')


class WelcomePageTest(myunit.MyTest):
    """欢迎页面修改资料测试"""
    def test_edit_myself(self):
        """测试修改个人资料"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = WelcomePage(self.driver)
        po2.to_edit_myself_page()
        sleep(5)
