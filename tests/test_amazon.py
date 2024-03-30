import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModule.AmazonPOM import Amazon

class TestAmazon:

    def test_amz(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.in/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

        self.Am=Amazon(self.driver)
        self.Am.search_product("iphone 15 pro max")
        print("This is a title:---",self.driver.title)
        self.Am.click_on_searchBtn()
        self.Am.all_products_name()
        print("pass")
        print("pass")
        print("pass")
        print("pass")
        print("Piyush Dravyakar")


        # self.window = self.driver.window_handles
        # print(self.window)
        # self.win = self.window[1]
        # self.driver.switch_to.window(self.win)
        # time.sleep(2)
        # print("This is a title:---",self.driver.title)
        # self.driver.execute_script("window.scrollBy(0,500)")
        # # self.Am.t




