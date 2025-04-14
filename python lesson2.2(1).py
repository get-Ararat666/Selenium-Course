from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID,"num2").text
    num1_int = int(num1)
    num2_int = int(num2)
    value_of_numbers = str(num1_int + num2_int)
    print(value_of_numbers)
    select = Select(browser.find_element(By.ID,"dropdown"))
    select.select_by_value(value_of_numbers)

    button = browser.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-default']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()