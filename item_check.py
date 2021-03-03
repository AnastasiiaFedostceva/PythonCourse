import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PythonCourse.base_class import BaseClass
from PythonCourse.actions import Actions
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
        regular_price_main_size = regular_price_main.value_of_css_property("font-size")

        campaign_price_main = driver.find_element_by_css_selector("strong.campaign-price")

        campaign_price_main_text = campaign_price_main.text
        campaign_price_main_color = check_color_to_string(campaign_price_main.value_of_css_property("color"))
        campaign_price_main_decorator = campaign_price_main.value_of_css_property("text-decoration")
        campaign_price_main_font_weight = campaign_price_main.value_of_css_property("font-weight")
        campaign_price_main_size = campaign_price_main.value_of_css_property("font-size")

        assert regular_price_main_color["red"] == regular_price_main_color["green"] == regular_price_main_color["blue"]
        assert campaign_price_main_color["green"] == "0" and campaign_price_main_color["blue"] == "0"
        assert "line-through" in regular_price_main_decorator
        assert not ("line-through" in campaign_price_main_decorator)
        assert int(regular_price_main_font_weight) in range(100, 501)
        assert int(campaign_price_main_font_weight) in range(600, 901)
        assert (float(regular_price_main_size[0:-2]) < float(campaign_price_main_size[0:-2]))

        item.click()

        item_name_item_page = driver.find_element_by_css_selector("div#box-product .title").text

        regular_price_item = driver.find_element_by_css_selector("s.regular-price")
        regular_price_item_color = check_color_to_string(regular_price_item.value_of_css_property("color"))
        regular_price_item_text = driver.find_element_by_css_selector("s.regular-price").text
        regular_price_item_decorator = \
            driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration")
        regular_price_item_font_weight = \
            driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-weight")
        regular_price_item_size = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font"
                                                                                                               "-size")

        campaign_price_item = driver.find_element_by_css_selector("strong.campaign-price")
        campaign_price_item_color = check_color_to_string(campaign_price_item.value_of_css_property("color"))
        campaign_price_item_text = driver.find_element_by_css_selector("strong.campaign-price").text
        campaign_price_item_decorator = \
            driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("text-decoration")
        campaign_price_item_font_weight = \
            driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
        campaign_price_item_size = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size")

        assert regular_price_item_color["red"] == regular_price_item_color["green"] == regular_price_item_color["blue"]
        assert campaign_price_item_color["green"] == "0" and campaign_price_item_color["blue"] == "0"
        assert "line-through" in regular_price_item_decorator
        assert not ("line-through" in campaign_price_item_decorator)
        assert int(regular_price_item_font_weight) in range(100, 501)
        assert int(campaign_price_item_font_weight) in range(600, 901)
        assert (float(regular_price_item_size[0:-2]) < float(campaign_price_item_size[0:-2]))

        assert item_name == item_name_item_page
        assert regular_price_main_text == regular_price_item_text
        assert campaign_price_main_text == campaign_price_item_text

    def item_creation(driver, item):
        wait = WebDriverWait(driver, 10)
        time.sleep(1)

        wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']")))
        driver.find_element_by_xpath("//span[text()='Catalog']").click()

        wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()=' Add New Product']")))
        driver.find_element_by_xpath("//a[text()=' Add New Product']").click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//h1[text()=' Add New Product']")))

        # General
        driver.find_element_by_xpath("//strong[text()='Status']/../label[text()=' Enabled']/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("//strong[text()='Name']/..//input").send_keys(item)
        time.sleep(3)
        driver.find_element_by_xpath("//strong[text()='Code']/..//input").send_keys("00000")
        Actions.checkbox_status(driver, "//input[@data-name='Rubber Ducks']")
        Actions.checkbox_status(driver, "//td[text()='Unisex']/../td/input")
        driver.find_element_by_css_selector("input[name=quantity]").send_keys(100)
        select_status = Select(driver.find_element_by_css_selector("select[name=sold_out_status_id]"))
        select_status.select_by_visible_text("Temporary sold out")
        time.sleep(2)
        driver.find_element_by_css_selector("input[name='new_images[]']").send_keys(os.path.join(os.path.dirname(__file__),'attachments', 'rock.jpg'))
        time.sleep(2)
        driver.find_element_by_css_selector("input[name=date_valid_from]").send_keys("01.01.2021")
        driver.find_element_by_css_selector("input[name=date_valid_to]").send_keys("31.12.2025")

        # Information
        driver.find_element_by_xpath("//a[text()='Information']").click()
        time.sleep(1)

        select_manufacturer = Select(driver.find_element_by_css_selector("select[name=manufacturer_id]"))
        select_manufacturer.select_by_visible_text("ACME Corp.")
        driver.find_element_by_css_selector("input[name=keywords]").send_keys("Duck")
        driver.find_element_by_css_selector("input[name='short_description[en]']").send_keys(
            "Short desc")
        driver.find_element_by_css_selector("div.trumbowyg-editor").send_keys("Item desc")
        driver.find_element_by_css_selector("input[name='head_title[en]']").send_keys(item)
        driver.find_element_by_css_selector("input[name='meta_description[en]']").send_keys(item)

        # Prices
        driver.find_element_by_xpath("//a[text()='Prices']").click()
        time.sleep(1)

        driver.find_element_by_css_selector("input[name=purchase_price]").send_keys("12,00")
        select_currency = Select(driver.find_element_by_css_selector("select[name=purchase_price_currency_code]"))
        select_currency.select_by_visible_text("Euros")
        driver.find_element_by_css_selector("input[name='prices[USD]']").send_keys("10.00")
        driver.find_element_by_css_selector("input[name='prices[EUR]']").send_keys("12.00")

        # Save
        driver.find_element_by_css_selector("button[name=save]").click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))


