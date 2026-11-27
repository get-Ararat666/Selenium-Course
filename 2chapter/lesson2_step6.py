import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,"input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer').send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()

    radbutton = browser.find_element(By.ID,'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radbutton)
    radbutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(9)
    browser.quit()