import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Amazon:
    search_id = "twotabsearchtextbox"
    search_btn_id = "nav-search-submit-button"
    products_names_xpath = "//div/h2/a/span" #need here loop , Apple iPhone 15 Pro (128 GB) - Natural Titanium
    add_to_cart_btn_Xpath = "(//span[text()='Add to Cart'])[2]"
    proceed_to_check_class = "a-button-input"

    def __init__(self,driver):
        self.driver = driver

    def search_product(self,product):
        self.driver.find_element(By.ID, self.search_id).send_keys(product)

    def click_on_searchBtn(self):
        self.driver.find_element(By.ID,self.search_btn_id).click()

    def all_products_name(self):
        self.All_products = self.driver.find_elements(By.XPATH, self.products_names_xpath)
        for self.all_product in self.All_products:
            print(self.all_product.text)
            if self.all_product.text == "Apple iPhone 15 Pro (1 TB) - White Titanium":
                self.all_product.click()
                print("clicked on selected product")


    def click_on_add_to_cart(self):
        self.driver.find_element(By.XPATH, "//span[text()='Add to Cart']").click()

    def click_on_proceed(self):
        self.driver.find_element(By.CLASS_NAME, self.proceed_to_check_class).click()



