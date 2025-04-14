from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID,"input_value").text
    y = calc(x)

    input = browser.find_element(By.ID,"answer")
    input.send_keys(y)

    browser.execute_script("window.scrollBy(0,200);")

    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()

    radiobox = browser.find_element(By.ID,"robotsRule")
    radiobox.click()

    button = browser.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-primary']")
    button.click()



finally:
    time.sleep(10)
    browser.quit()