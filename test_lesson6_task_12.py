import pytest
from selenium import webdriver
from PythonCourse.login import Login
from PythonCourse.item_check import Item
import os

@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_lesson6_task_12_chrome(chrome_driver):
    Login.login(chrome_driver)
    item = 'Rocks duck 03'
    Item.item_creation(chrome_driver, item)

    res = chrome_driver.find_elements_by_xpath(f"//table[@class='dataTable']//a[text()='{item}']")
    assert len(res) == 1

