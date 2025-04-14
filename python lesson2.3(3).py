from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR,"button[class = 'trollface btn btn-primary']").click()

    next_page = browser.window_handles[1]
    browser.switch_to.window(next_page)

    element_x = browser.find_element(By.ID,"input_value")
    x = element_x.text
    y = calc(x)

    input = browser.find_element(By.ID,"answer").send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-primary']").click()

finally:
    time.sleep(10)
    browser.quit()