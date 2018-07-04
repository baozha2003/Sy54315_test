from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.codeprint_page import CodPrintPage
import requests

sys.path.append('./models')
sys.path.append('./page_obj')


class CodePrintTest(myunit.MyTest):
    """赋码打印页面测试"""

    def test_codeprint_search(self):
        """测试搜索功能"""
        # 登陆
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = CodPrintPage(self.driver)
        sleep(1)
        # 进入赋码打印页
        po2.to_codprint_link()
        # 进行搜索操作
        po2.breedname_search_case()
        sleep(0.5)
        # 结果断言
        self.assertEqual(po2.result_batch_no(), 'ZZ2018053100006')
        function.insert_img(self.driver, 'codeprint_search_result.png')

    def test_codeprint(self):
        """赋码打印接口测试"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        # sleep(1)
        # po2 = CodPrintPage(self.driver)
        # sleep(0.5)
        # po2.to_codprint_link()
        # po2.frist_codprint_button()
        # sleep(3)
        # 获取登陆后的cookies
        cookies = po.get_cookies()
        ucsid = cookies[0]['value']
        url = "http://sytest.54315.com/codeprint/print"

        querystring = {"packId": "363"}

        headers = {
            'Cookie': "ucsid=%s" % ucsid
        }
        # 访问赋码打印接口
        response = requests.request("GET", url, headers=headers, params=querystring)
        # 断言
        self.assertIn('"code":"100","message":"success"', response.text)
        print(response.text)
        # function.insert_img(self.driver, 'codeprint_success.png')
