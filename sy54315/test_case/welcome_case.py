from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.welcome_page import WelcomePage
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.base import Base

sys.path.append('./models')
sys.path.append('./page_obj')


class WelcomePageTest(myunit.MyTest):
    """欢迎页面修改资料测试"""

    def test_edit_myself(self):
        """测试修改个人资料"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        po2 = WelcomePage(self.driver)
        po2.to_edit_myself_page()
        function.insert_img(self.driver, 'edit_successful_result.png')
        self.assertEqual(po2.submit_successful_result(), '编辑个人资料成功')
        # Base.WaitElem(po2.driver, '/html/body/header/ul/li[2]/p/a[1]')

    def test_changepwd(self):
        """测试修改密码"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        po2 = WelcomePage(self.driver)
        po2.to_changepwd()
        self.assertEqual(po2.changepwd_successful_result(), '修改密码成功,请使用新密码重新登录')
        function.insert_img(self.driver, 'changepwd_successful_result.png')
