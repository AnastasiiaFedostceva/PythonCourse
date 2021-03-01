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


def test_lesson5_task_9_2_chrome(chrome_driver):
    Login.login(chrome_driver)
    url1 = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"
    chrome_driver.get(url1)

    county_elem_list = chrome_driver.find_elements_by_css_selector("form[name=geo_zones_form] td:nth-of-type(3) a")

    # Countries with zones
    country_names = []
    for c in county_elem_list:
        country_names.append(c.text)
    print(country_names)

    # Get zones list
    for country_name in country_names:
        time.sleep(2)

        chrome_driver.find_element_by_xpath(f"//form[@name='geo_zones_form']//a[text()='{country_name}']").click()

        zone_list_shown = chrome_driver.find_elements_by_css_selector("table#table-zones select[name*=zone_code]")
        zone_list = []
        for zones in zone_list_shown:
            zone = zones.find_element_by_css_selector("option[selected]").text
            zone_list.append(zone)

        zone_list_exp = sorted(zone_list)
        assert zone_list == zone_list_exp

        chrome_driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

