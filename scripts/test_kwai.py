import sys,os
sys.path.append(os.getcwd())
import page
from base.base_driver import base_driver
from page.navigation_page import Navigation
class TestKwai:
    def setup_class(self):
        self.driver = base_driver("com.smile.gifmaker","com.yxcorp.gifshow.HomeActivity")
        self.navigation = Navigation(self.driver)
    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.navigation.get_home_page_obj().click_login(15803391962)
        # self.driver.find_element_by_id("com.smile.gifmaker:id/left_text_two").click()