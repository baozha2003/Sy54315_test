from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage

sys.path.append('./model')
sys.path.append('./page_obj')


class LoginTest(myunit.MyTest):
    """测试登陆"""

    def test_login_user_pwd_success(self):
        """测试正常Login"""
        po = LoginPage(self.driver)
        po.open()
        user = "13727086330"
        po.login_action(user, "qwe123")
        sleep(2)
        function.insert_img(self.driver, "Login_success.png")

    def test_login_Null(self):
        """账户密码为空"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action("", "")
        sleep(2)
        self.assertEqual(po.login_error_hint(),"手机号不能为空！")
        function.insert_img(self.driver,"Login_Nullerror.png")