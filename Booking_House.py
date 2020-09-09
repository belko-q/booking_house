from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
browser.find_element_by_xpath("//button[@id='book']").click()

x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = int(x_element.text)
z = str(math.log(abs(12*math.sin(x))))
browser.find_element_by_xpath("//input[@id='answer']").send_keys(z)

button = browser.find_element_by_xpath("//button[@type='submit']").click()
