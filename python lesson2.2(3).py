from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-primary']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    y = calc(x)

    input = browser.find_element(By.ID,"answer")
    input.send_keys(y)

    sumbit = browser.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-primary']")
    sumbit.click()


finally:
    time.sleep(10)
    browser.quit()