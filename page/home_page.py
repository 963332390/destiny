import page
from base.base_actions import BaseActions
class HomePage(BaseActions):

    def __init__(self,driver):
        BaseActions.__init__(self,driver)

    def click_login(self,num):
        self.click_element(page.home_page_login_in_id)
        self.click_element(page.login_page_phone_login_id)
        self.send_element(page.login_page_phone_login_input_id,num)
        self.click_element(page.login_page_next_btn_id)