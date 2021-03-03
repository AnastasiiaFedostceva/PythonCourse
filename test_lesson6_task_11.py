import pytest
from selenium import webdriver

from PythonCourse.actions import Actions
from PythonCourse.registration import Registration
from PythonCourse.login import Login

@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_lesson6_task_11_chrome(chrome_driver):
    email = "{}@mailinator.com".format(Actions.randomString())
    password = '12345'

    Registration.registration(chrome_driver, email, password)
    Login.user_login(chrome_driver, email, password)