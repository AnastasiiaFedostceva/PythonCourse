import time

from PythonCourse.base_class import BaseClass


class Actions(BaseClass):

    def is_element_present(locator, driver):
        return len(driver.find_elements_by_css_selector(locator)) > 0

    def click(css_locator, driver):
        driver.find_element_by_css_selector(css_locator).click()
        time.sleep(1)