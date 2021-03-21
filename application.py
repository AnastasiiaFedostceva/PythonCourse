from selenium import webdriver

from PythonCourse.helpers.cartPage import CartPageHelper
from PythonCourse.helpers.itemPage import ItemPageHelper
from PythonCourse.helpers.mainPage import MainPageHelper

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver



class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)

class Application:


    def __init__(self, browser="chrome"):
        capabilities = {"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}}

        if browser == "chrome":
            self.driver = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=capabilities), MyListener())
        elif browser == "firefox":
            self.driver = EventFiringWebDriver(
                webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe",
                                  desired_capabilities=capabilities), MyListener())


        self.driver.implicitly_wait(2)

        # =========== HELPERS ===========
        self.main = MainPageHelper(self.driver)
        self.cart = CartPageHelper(self.driver)
        self.item = ItemPageHelper(self.driver)