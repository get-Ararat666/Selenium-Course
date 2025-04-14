import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y=calc(x)


    inp = browser.find_element(By.CLASS_NAME, "form-control")
    inp.send_keys(y)

    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element(By.ID, "robotsRule")
    radiobox.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-default']")
    button.click()
finally:
    time.sleep(20)
    browser.quit()