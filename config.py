import pytest
from PythonCourse.application import Application


@pytest.fixture()
def app(request):
    def teardown():
        fixture.wd.quit()
    try:
        fixture = Application(request.param)
    except AttributeError:
        fixture = Application()
    request.addfinalizer(teardown)
    return fixture