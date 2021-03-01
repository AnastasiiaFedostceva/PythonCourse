import pytest
from selenium import webdriver
from PythonCourse.actions import Actions
from PythonCourse.login import Login


@pytest.fixture
def chrome_driver(request):
    wd = chrome_driver.Chrome = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_lesson5_task_9_1_chrome(chrome_driver):
    Login.login(chrome_driver)
    url1 = "http://localhost/litecart/admin/?app=countries&doc=countries"
    chrome_driver.get(url1)

    country_rows_list = chrome_driver.find_elements_by_css_selector("form[name=countries_form] tr.row")

    country_list = []
    country_with_zones_list = []

    # Get the list of countries
    for country_row in country_rows_list:
        zones = country_row.find_element_by_css_selector("td:nth-of-type(6)").text
        country_name = country_row.find_element_by_css_selector("td:nth-of-type(5) a").text
        country_list.append(country_name)
        if zones != "0":
            country_with_zones_list.append(country_name)

    # Check countries sorting
    country_list_exp = sorted(country_list)
    assert country_list == country_list_exp

    # Get the list of zones
    for country_name in country_with_zones_list:
        chrome_driver.find_element_by_xpath(f"//form[@name='countries_form']//a[text() = '{country_name}']").click()

        zone_el_list = chrome_driver.find_elements_by_css_selector("table.dataTable td:nth-of-type(3)")[:-1]
        zone_list = []

        for zone_el in zone_el_list:
            zone_list.append(zone_el.text)

        chrome_driver.get(url1)

        # Check zone's sorting
        zone_list_exp = sorted(zone_list)
        assert zone_list == zone_list_exp
