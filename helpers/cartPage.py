from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPageHelper:

    def __init__(self, driver):
        self.driver = driver

    def get_items_count(self):
        count = len(self.driver.find_elements_by_css_selector("li.shortcut"))
        if count == 0:
            items_count = 1
        else:
            items_count = count
        return items_count

    def select_first_item(self):
        if len(self.driver.find_elements_by_css_selector("li.shortcut")) > 0:
            self.driver.find_elements_by_css_selector("li.shortcut")[0].click()

    def remove_first_item(self):
        self.select_first_item()

        table = self.driver.find_element_by_css_selector("div#order_confirmation-wrapper table")

        self.driver.find_elements_by_css_selector("button[name=remove_cart_item]")[0].click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.staleness_of(table))