import pytest
from selenium import webdriver
from PythonCourse.actions import Actions
from PythonCourse.login import Login


@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_lesson4_task_8_chrome(chrome_driver):
    chrome_driver.get("http://localhost/litecart/")
    li_list = chrome_driver.find_elements_by_css_selector("li.product")

    for li in li_list:
        assert len(li.find_elements_by_css_selector(".sticker")) == 1