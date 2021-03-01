from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonCourse.base_class import BaseClass
import re


def check_color_to_string(str):
    result = re.search(r"rgba?\((\d+), (\d+), (\d+)(, \d+)?\)", str)
    return {
        "red": result[1],
        "green": result[2],
        "blue": result[3]
    }


class Item(BaseClass):

    def item_check(driver):
        driver.get("http://localhost/litecart/en/")
        item = driver.find_element_by_css_selector("div#box-campaigns a.link")

        item_name = item.find_element_by_css_selector("div.name").text

        regular_price_main = item.find_element_by_css_selector("s.regular-price")
        regular_price_main_text = regular_price_main.text
        regular_price_main_color = check_color_to_string(regular_price_main.value_of_css_property("color"))
        regular_price_main_decorator = regular_price_main.value_of_css_property("text-decoration")
        regular_price_main_font_weight = regular_price_main.value_of_css_property("font-weight")
        regular_price_main_size = regular_price_main.size

        campaign_price_main = driver.find_element_by_css_selector("strong.campaign-price")

        campaign_price_main_text = campaign_price_main.text
        campaign_price_main_color = check_color_to_string(campaign_price_main.value_of_css_property("color"))
        campaign_price_main_decorator = campaign_price_main.value_of_css_property("text-decoration")
        campaign_price_main_font_weight = campaign_price_main.value_of_css_property("font-weight")
        campaign_price_main_size = campaign_price_main.size

        assert regular_price_main_color["red"] == regular_price_main_color["green"] == regular_price_main_color["blue"]
        assert campaign_price_main_color["green"] == "0" and campaign_price_main_color["blue"] == "0"
        assert "line-through" in regular_price_main_decorator
        assert not ("line-through" in campaign_price_main_decorator)
        assert int(regular_price_main_font_weight) in range(100, 501)
        assert int(campaign_price_main_font_weight) in range(600, 901)
        assert (regular_price_main_size["height"] < campaign_price_main_size["height"] and
                regular_price_main_size["width"] < campaign_price_main_size["width"])

        item.click()

        item_name_item_page = driver.find_element_by_css_selector("div#box-product .title").text

        regular_price_item = driver.find_element_by_css_selector("s.regular-price")
        regular_price_item_color = check_color_to_string(regular_price_item.value_of_css_property("color"))
        regular_price_item_text = driver.find_element_by_css_selector("s.regular-price").text
        regular_price_item_decorator = \
            driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration")
        regular_price_item_font_weight = \
            driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-weight")
        regular_price_item_size = driver.find_element_by_css_selector("s.regular-price").size

        campaign_price_item = driver.find_element_by_css_selector("strong.campaign-price")
        campaign_price_item_color = check_color_to_string(campaign_price_item.value_of_css_property("color"))
        campaign_price_item_text = driver.find_element_by_css_selector("strong.campaign-price").text
        campaign_price_item_decorator = \
            driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("text-decoration")
        campaign_price_item_font_weight = \
            driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
        campaign_price_item_size = driver.find_element_by_css_selector("strong.campaign-price").size

        assert regular_price_item_color["red"] == regular_price_item_color["green"] == regular_price_item_color["blue"]
        assert campaign_price_item_color["green"] == "0" and campaign_price_item_color["blue"] == "0"
        assert "line-through" in regular_price_item_decorator
        assert not ("line-through" in campaign_price_item_decorator)
        assert int(regular_price_item_font_weight) in range(100, 501)
        assert int(campaign_price_item_font_weight) in range(600, 901)
        assert (regular_price_item_size["height"] < campaign_price_item_size["height"] and
                regular_price_item_size["width"] < campaign_price_item_size["width"])

        assert item_name == item_name_item_page
        assert regular_price_main_text == regular_price_item_text
        assert campaign_price_main_text == campaign_price_item_text
