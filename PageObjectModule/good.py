import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)

path  = driver.find_element(By.ID, "dropdown-class-example")
select = Select(path)

select.select_by_value("option3")

time.sleep(3)

checks = driver.find_elements(By.XPATH, "//label")
inputs = driver.find_elements(By.XPATH, "//label/input")

for check,input in zip(checks,inputs):
    print(check.text)
    # inputs = driver.find_elements(By.XPATH, "//label/input")
    if check.text == "Option3":
        input.click()


dropdown = driver.find_element(By.ID, "autocomplete")

dropdown.click()
dropdown.send_keys("Ind")

suggestions = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")

for suggestion in suggestions:
    print(suggestion.text)
    if suggestion.text == "British Indian Ocean Territory":
        suggestion.click()


names_radio = driver.find_elements(By.XPATH, "//label")
inputs_radio = driver.find_elements(By.XPATH, "//label/input")

for names,rads in zip(names_radio,inputs_radio):
    print(names.text)
    if names.text == "Radio3":
        rads.click()
print("******************************************************************************")
print(driver.title)
#new window

driver.find_element(By.ID, "openwindow").click()

windows = driver.window_handles
print(windows)
wind = windows[1]
winds = windows[0]
driver.switch_to.window(wind)
print(driver.title)

text_printss = driver.find_elements(By.XPATH, "//div/p")

for textss in text_printss:
    print(textss.text)
    if textss.text == "Welcome to our online software testing academy!":
        break

driver.switch_to.window(winds)
time.sleep(1)
print("This is title:-- ", driver.title)

time.sleep(3)


#alerts

driver.find_element(By.ID, "name").send_keys("piyush")
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alerts = driver.switch_to.alert
alerts.accept()
