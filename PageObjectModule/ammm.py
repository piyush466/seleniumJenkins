from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Apple-iPhone-15-256-GB/dp/B0CHX6N27Y/ref=sr_1_8?crid=1DHXUTVT7U219&dib=eyJ2IjoiMSJ9.8-aKrERwPzdGyJWfWOa56GxHt3lPSumQdiYENOIE4aRhDPQn-fIYfKJxxKAv6p4vGhXGfOYZfq84YAK8MIW2g8EJxFNluIQneY__A6MK-7OiccMisPJwAjUCwcI2X9w42kpgfyCs4_8bolv2gAThweJFM1s1DHSdT9tfQ8ofmnRazMPeUrc5s9_CYnsCg5X6na6CnGkzsi_MomIAJM08Vc4b7eBi9mIl5lBksd8-wLI.8kr2lqt39xHhEuoy4X6JGc02hT0bClJpx9dpOyiNf8k&dib_tag=se&keywords=iphone+15&qid=1711365726&sprefix=iphone+15+%2Caps%2C238&sr=8-8")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to Cart']")))
add_to_cart_button.click()
