from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.process_page import ProcessPage


class ProcessTest(myunit.MyTest):
    """初加工计划页面测试用例"""

    def test_process_search(self):
        """初加工任务搜索"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = ProcessPage(self.driver)
        po2.to_process_page()
        po2.breedName_search_text("金银花")
        po2.choose_medSource_select(1)
        po2.search_button_click()
        sleep(1)
        self.assertEqual(po2.frist_line_breedName(),"金银花")
        function.insert_img(self.driver,'search_process_reresult.png')

