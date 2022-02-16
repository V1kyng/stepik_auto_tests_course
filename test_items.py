import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_exist(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button = browser.find_element_by_css_selector('#add_to_basket_form > button')
    time.sleep(30)
    assert button.text is not None
