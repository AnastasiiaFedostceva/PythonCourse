import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from PythonCourse.application import Application


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

@pytest.fixture()
def app(request):
    def teardown():
        fixture.driver.quit()
    try:
        fixture = Application(request.param)
    except AttributeError:
        fixture = Application()
    request.addfinalizer(teardown)
    return fixture


def test_lesson11_task_19_chrome(app):
    for _ in range(3):
        app.main.select_item()
        app.item.add_item_to_cart()

    app.main.open_cart()

    for _ in range(app.cart.get_items_count()):
        app.cart.remove_first_item()
