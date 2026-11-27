import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname").send_keys("Misha")
    second_name = browser.find_element(By.NAME, "lastname").send_keys("Pirozhnikov")
    email = browser.find_element(By.NAME, "email").send_keys("mishapriog228@gmial.com")

    file_txt = browser.find_element(By.ID, 'file').send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
                                  

finally:
    time.sleep(9)
    browser.quit()