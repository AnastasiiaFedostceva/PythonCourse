from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonCourse.base_class import BaseClass


class Login(BaseClass):
    def login(driver):
        credential_login = "admin"
        credential_pass = "admin"
        xpath_login_btn = '//*[@id="box-login"]/form/div[2]/button'
        xpath_logo = '//*[@id="sidebar"]/div[1]/a/img'
        url = 'http://localhost/litecart/admin/'
        driver.get(url)

        elements_name = driver.find_element_by_name("username")
        if not elements_name:
            driver.quit()
        else:
            elements_name.send_keys(credential_login)

        elements_pass = driver.find_element_by_name("password")
        if not elements_pass:
            driver.quit()
        else:
            elements_pass.send_keys(credential_pass)

        elements_login_btn = driver.find_element_by_xpath(xpath_login_btn)
        if not elements_login_btn:
            driver.quit()
        else:
            elements_login_btn.click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath_logo)))

        element.click()

    def user_login(driver, email, password):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=email]")))

        driver.find_element_by_css_selector("input[name=email]").send_keys(email)
        driver.find_element_by_css_selector("input[name=password]").send_keys(password)
        driver.find_element_by_css_selector("button[name=login]").click()

        wait = WebDriverWait(driver, 3)

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))
        driver.find_element_by_xpath("//a[text()='Logout']").click()