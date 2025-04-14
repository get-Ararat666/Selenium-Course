from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    treasure = browser.find_element(By.ID,"treasure")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input = browser.find_element(By.ID,"answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()

    radiobox = browser.find_element(By.ID,"robotsRule")
    radiobox.click()

    button = browser.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-default']")
    button.click()




finally:
    time.sleep(10)
    browser.quit()