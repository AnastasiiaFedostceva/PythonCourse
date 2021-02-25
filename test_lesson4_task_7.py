import time

import pytest
from selenium import webdriver
from PythonCourse.actions import Actions
from PythonCourse.login import Login


@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_lesson4_task_7_chrome(chrome_driver):
    Login.login(chrome_driver)

    li_list = chrome_driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")

    i = 1
    for _ in li_list:
        loc_li = f"li#app-:nth-child({i})"
        Actions.click(loc_li, chrome_driver)

        loc_ul = f"{loc_li} ul.docs"
        if Actions.is_element_present(loc_ul, chrome_driver):
            j = 1
            li_nested_list = chrome_driver.find_elements_by_css_selector(f"{loc_ul} li")

            for _ in li_nested_list:
                loc_li_nested = f"{loc_ul} li:nth-child({j})"
                Actions.click(loc_li_nested, chrome_driver)
                assert Actions.is_element_present("h1", chrome_driver)
                j += 1
        #assert Actions.is_element_present("h1", chrome_driver)
        i += 1
