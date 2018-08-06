from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.base import Base

sys.path.append('./models')
sys.path.append('./page_obj')


class LoginTest(myunit.MyTest):
    """测试登陆"""

    def test_login_user_pwd_success(self):
        """测试正常Login"""
        po = LoginPage(self.driver)
        po.open()
        user = "13727086330"
        po.login_action(user, "qwe123")
        function.insert_img(self.driver, "Login_success.png")

    def test_login_Null(self):
        """账户密码为空"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action("", "")
        nowtime = Base(self.driver).now_time()
        try:
            self.assertEqual(po.login_error_hint(), "手机号不能为空！")
        except:
            # function.insert_img(self.driver, "Login_Nullerror.png")
            function.insert_img(self.driver, '%s.png'% nowtime )