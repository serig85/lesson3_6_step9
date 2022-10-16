from selenium.webdriver.common.by import By
import time


def test_guest_should_see_btn_add_to_basket(browser):
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    time.sleep(5)
    

