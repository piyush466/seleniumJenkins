import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
# time.sleep(3)
products_names = driver.find_elements(By.XPATH, "//div[@class='product']/h4")
Buttons = driver.find_elements(By.XPATH, "//div[@class='product']/div/button")
for products_name,button in zip(products_names,Buttons):
    print(products_name.text)
    if products_name.text == "Cucumber - 1 Kg":
        button.click()
        break


driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

All_pri = driver.find_elements(By.XPATH, "//div/b")

for pri in All_pri:
    print(pri.text)


driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/input').send_keys("Piyush")

driver.find_element(By.XPATH, "//button[text()='Apply']").click()

#print empty

print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()

driver.find_element(By.XPATH, '//select').click()

contries = driver.find_elements(By.XPATH, "//option")

for contry in contries:
    print(contry.text)
    if contry.text == "India":
        contry.click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/input').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()






time.sleep(4)

