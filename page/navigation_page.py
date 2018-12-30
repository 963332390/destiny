from page.home_page import HomePage
class Navigation:

    def __init__(self,driver):
        self.driver = driver

    def get_home_page_obj(self):
        return HomePage(self.driver)