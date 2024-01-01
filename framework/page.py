import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from logger.log import Logging

findby = {
    'ID': AppiumBy.ID,
    'XPATH': AppiumBy.XPATH,
    'CLASS_NAME': AppiumBy.CLASS_NAME,
    'NAME': AppiumBy.NAME,
    'TAG_NAME': AppiumBy.TAG_NAME,
    'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
    'IMAGE': AppiumBy.IMAGE,
    'CSS_SELECTOR': AppiumBy.CSS_SELECTOR,
    'WINDOWS_UI_AUTOMATION': AppiumBy.WINDOWS_UI_AUTOMATION,
    'TEXT': AppiumBy.LINK_TEXT,
    'ANDROID_UIAUTOMATOR': AppiumBy.ANDROID_UIAUTOMATOR,
}


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.logging = Logging()

    def find_element(self, strategy: str, selector: str):
        """Find element using strategy"""
        el = None

        try:
            el = self.driver.find_element(by=findby[strategy], value=selector)
            self.logging.element_logger(strategy, selector, el)
        except NoSuchElementException:
            while bool(el) is False:
                self.logging.wait_for_seconds(2)
                self.logging.logging_error('Element was not found. Trying to find it again...')
                self.logging.wait_for_seconds(2)
                try:
                    el = self.driver.find_element(by=findby[strategy], value=selector)
                    self.logging.logging_debug(f'We found the element? {bool(el)}')
                    if bool(el):
                        el = self.driver.find_element(by=findby[strategy], value=selector)
                        break
                except NoSuchElementException:
                    el = False
                    self.logging.logging_debug('Waiting for the element...')
        finally:
            self.logging.final_logger(el)
        return el

    def find_nested_element(self, strategy, selector, nested_strategy, nested_selector):
        """
        find a nested selenium element
        """
        self.logging.logging_debug('Start to find nested element\n')
        el = self.find_element(strategy, selector)
        self.click_element(el)
        nested_element = self.find_element(nested_strategy, nested_selector)
        self.click_element(nested_element)
        self.logging.logging_debug('Nested element was found\n')

    def find_elements(self, strategy: str, selector: str):
        """Find elements using strategy"""
        el_list = None

        try:
            el_list = self.driver.find_elements(by=findby[strategy], value=selector)
            self.logging.element_logger(strategy, selector, el_list)
        except NoSuchElementException:
            while bool(el_list) is False:
                self.logging.wait_for_seconds(2)
                self.logging.logging_error('Elements were not found. Trying to find them again...')
                self.logging.wait_for_seconds(2)
                try:
                    el_list = self.driver.find_elements(by=findby[strategy], value=selector)
                    self.logging.logging_debug(f'We found the elements? {bool(el_list)}')
                    if bool(el_list):
                        el_list = self.driver.find_element(by=findby[strategy], value=selector)
                        break
                except NoSuchElementException:
                    el_list = False
                    self.logging.logging_debug('Waiting for the elements...')
        finally:
            self.logging.final_logger(el_list)
        return el_list

    def click_element(self, element):
        element.click()
        self.logging.logging_info(f"Clicked on the element.")

    def input_keys(self, element, value: str):
        element.send_keys(value)
        self.logging.logging_info(f"Sent the keys {value} to the element")

    def select_from_menu(self, menu_strategy, menu_id, list_option_strategy, list_option_selector):
        self.logging.logging_debug(f'Trying to select option: {list_option_selector} for {menu_id}')
        menu = self.find_element(menu_strategy, menu_id)
        self.click_element(menu)

        self.logging.logging_debug('Checking for menu options')
        element = self.find_element(list_option_strategy, list_option_selector)
        self.click_element(element)

        time.sleep(5)
