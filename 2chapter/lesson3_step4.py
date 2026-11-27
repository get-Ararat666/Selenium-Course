import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    start = browser.find_element(By.CSS_SELECTOR," .btn-primary").click()
    alert = browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input_x = browser.find_element(By.ID,'answer').send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, " .btn-primary").click()


finally:
    time.sleep(15)
    browser.quit()