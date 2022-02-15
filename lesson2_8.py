from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome('../drivers/chromedriver')
    # browser.implicitly_wait(3)
    browser.get(link)
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button.click()

    x = int(browser.find_element_by_css_selector('.form-group #input_value').text)
    funcx = math.log(abs(12 * math.sin(x)))
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(str(funcx))
    submit = browser.find_element_by_css_selector('#solve')
    submit.click()
    #assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()
