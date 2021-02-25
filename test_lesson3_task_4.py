import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PythonCourse.login import Login


@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def edge_driver(request):
    wd = webdriver.Edge()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def firefox_driver(request):
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    wd = firefox_driver.Firefox = webdriver.Firefox(
        executable_path=r'C:\Selenium\geckodriver\geckodriver.exe', firefox_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_lesson_3_task4_firefox(firefox_driver):
    Login.login(firefox_driver)


def test_lesson_3_task4_chrome(chrome_driver):
    Login.login(chrome_driver)


def test_lesson_3_task4_edge(edge_driver):
    Login.login(edge_driver)
