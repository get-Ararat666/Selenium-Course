import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    img_treasure = browser.find_element(By.ID, 'treasure')
    get_number = img_treasure.get_attribute("valuex")

    y = calc(get_number)

    input_x = browser.find_element(By.ID,'answer').send_keys(y)

    checkbox = browser.find_element(By.ID,'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID, 'robotsRule').click()

    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-default').click()


finally:
    time.sleep(10)
    browser.quit()