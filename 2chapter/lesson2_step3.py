import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID,'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    total = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(total)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(8)
    browser.quit()