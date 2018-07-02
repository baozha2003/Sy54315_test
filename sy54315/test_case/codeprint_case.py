from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.codeprint_page import CodPrintPage

sys.path.append('./models')
sys.path.append('./page_obj')


class CodePrintTest(myunit.MyTest):
    """赋码打印页面测试"""

    def test_codeprint_search(self):
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = CodPrintPage(self.driver)
        sleep(1)
        po2.to_codprint_link()
        po2.breedname_search_case()
        sleep(0.5)
        self.assertEqual(po2.result_batch_no(), 'ZZ2018053100006')
        function.insert_img(self.driver, 'codeprint_search_result.png')

    def test_codeprint(self):
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = CodPrintPage(self.driver)
        sleep(0.5)
        po2.to_codprint_link()
        po2.frist_codprint_button()
        sleep(3)
        function.insert_img(self.driver, 'codeprint_success.png')
