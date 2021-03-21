import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPageHelper:

    def __init__(self, driver):
        self.driver = driver

    def select_item(self):
        url = "http://localhost/litecart/en/"
        self.driver.get(url)
        self.driver.find_elements_by_css_selector("div#box-most-popular li.product")[0].click()

    def open_cart(self):
        self.driver.find_element_by_xpath("//a[text()='Checkout »']").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#order_confirmation-wrapper table")))
        time.sleep(1)