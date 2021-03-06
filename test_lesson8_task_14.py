import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PythonCourse.login import Login
from PythonCourse.countries import Countries

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

def test_lesson8_task_14_chrome(chrome_driver):
    Login.login(chrome_driver)
    Countries.open_country_link(chrome_driver)
    Countries.create_new_country(chrome_driver)
    Countries.open_external_link_in_new_window(chrome_driver)


