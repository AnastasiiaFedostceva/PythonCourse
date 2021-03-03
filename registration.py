import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from PythonCourse.base_class import BaseClass


class Registration(BaseClass):

    def registration(driver, email, password):
        driver.get("http://localhost/litecart/en/")
        driver.find_element_by_xpath("//a[text()='New customers click here']").click()

        time.sleep(1)

        driver.get("http://localhost/litecart/en/")
        driver.find_element_by_xpath("//a[text()='New customers click here']").click()

        time.sleep(1)

        driver.find_element_by_css_selector("input[name=firstname]").send_keys("TestFirstName")
        driver.find_element_by_css_selector("input[name=lastname]").send_keys("TestLastName")
        driver.find_element_by_css_selector("input[name=address1]").send_keys("Test")
        driver.find_element_by_css_selector("input[name=postcode]").send_keys("12345")
        driver.find_element_by_css_selector("input[name=city]").send_keys("City")
        driver.find_element_by_css_selector("input[name=email]").send_keys(email)
        driver.find_element_by_css_selector("input[name=phone]").send_keys("12345")
        driver.find_element_by_css_selector("input[name=password]").send_keys(password)
        driver.find_element_by_css_selector("input[name=confirmed_password]").send_keys(password)

        ActionChains(driver).click(driver.find_element_by_css_selector("span.select2-selection")) \
            .send_keys("United States").send_keys(Keys.ENTER).perform()

        ActionChains(driver).click(driver.find_element_by_css_selector("select[name=zone_code]")) \
            .send_keys("Colorado").send_keys(Keys.ENTER).perform()

        driver.find_element_by_css_selector("button[name=create_account]").click()

        time.sleep(1)

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))
        driver.find_element_by_xpath("//a[text()='Logout']").click()

