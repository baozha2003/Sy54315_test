import unittest
from .driver import browser


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser('Phantomjs')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
