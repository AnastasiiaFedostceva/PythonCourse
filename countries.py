import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium.webdriver.support.wait import WebDriverWait

from PythonCourse.base_class import BaseClass
from PythonCourse.windows_mgmt import WindowManagementWait


class Countries(BaseClass):
    def open_country_link(driver):
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//h1[text()=' Countries']")))

    def create_new_country(driver):
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()=' Add New Country']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h1[text()=' Add New Country']")))

    def open_external_link_in_new_window(driver):
        external_links_list = driver.find_elements_by_css_selector("i.fa-external-link")
        list_length = len(external_links_list)
        main_window = driver.current_window_handle

        for i in range(list_length):
            old_windows = driver.window_handles
            driver.find_elements_by_css_selector("i.fa-external-link")[i].click()
            wait = WebDriverWait(driver, 10)
            new_window = wait.until(WindowManagementWait(old_windows))
            driver.switch_to_window(new_window)
            driver.close()
            driver.switch_to_window(main_window)
