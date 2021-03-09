import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PythonCourse.base_class import BaseClass


class Cart(BaseClass):
    def add_item_to_cart(driver):
        for _ in range(3):
            time.sleep(5)
            driver.get("http://localhost/litecart/en/")
            driver.find_elements_by_css_selector("div#box-most-popular li.product")[0].click()

            if len(driver.find_elements_by_css_selector("div.buy_now select")) > 0:
                ActionChains(driver).click(driver.find_element_by_css_selector("select[nameoptions[Size]")) \
                    .send_keys("Small").send_keys(Keys.ENTER).perform()

            time.sleep(5)
            driver.find_element_by_css_selector("button[name=add_cart_product]").click()

            quantity = driver.find_element_by_css_selector("span.quantity")
            item_count = quantity.text
            print(item_count)
            wait = WebDriverWait(driver, 10)
            wait.until_not(lambda d: d.find_element_by_name("span.quantity").text == item_count)

    def open_cart(driver):
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Checkout »']").click()
        shortcuts_num = len(driver.find_elements_by_css_selector("li.shortcut"))

        if shortcuts_num == 0:
            items_count = 1
        else:
            items_count = shortcuts_num
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#order_confirmation-wrapper table")))
        time.sleep(1)
        return items_count

    def delete_item_from_cart(driver, items_count):
        for _ in range(items_count):
            if len(driver.find_elements_by_css_selector("li.shortcut")) > 0:
                time.sleep(5)
                driver.find_elements_by_css_selector("li.shortcut")[0].click()

            order_summary = driver.find_element_by_css_selector("div#order_confirmation-wrapper table")
            time.sleep(5)
            driver.find_elements_by_css_selector("button[name=remove_cart_item]")[0].click()

            wait = WebDriverWait(driver, 10)
            wait.until(ec.staleness_of(order_summary))