from time import sleep
import sys
from sy54315.test_case.models import function, myunit
from sy54315.test_case.page_obj.login_page import LoginPage
from sy54315.test_case.page_obj.plant_page import PlantPage
from sy54315.test_case.page_obj.medpack_page import MedPackPage
from sy54315.test_case.page_obj.addplant_page import AddPlantPage
from sy54315.test_case.page_obj.addplant_task_page import AddPlantTaskPage

sys.path.append('./models')
sys.path.append('./page_obj')


class MedPackTest(myunit.MyTest):
    """分包页面测试"""

    def test_upload_quality_data(self):
        """上传质检数据"""
        po = LoginPage(self.driver)
        po.open()
        po.login_action(13727086330, "qwe123")
        sleep(1)
        po2 = MedPackPage(self.driver)
        po2.to_medpack_page()
        po2.quality_data_upload()
        sleep(1)
        self.assertEqual(po2.subpackage_successful_text(),'上传成功!')
        function.insert_img(self.driver, "subpackage_successful.png")