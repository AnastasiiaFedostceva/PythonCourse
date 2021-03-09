import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PythonCourse.cart import Cart

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

def test_lesson7_task_13_chrome(chrome_driver):

    cart = Cart
    cart.add_item_to_cart(chrome_driver)
    items_count = cart.open_cart(chrome_driver)
    cart.delete_item_from_cart(chrome_driver, items_count)
