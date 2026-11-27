import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    text1 = browser.find_element(By.ID, 'answer').send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID,'robotsRule').click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(30)
    browser.quit()
