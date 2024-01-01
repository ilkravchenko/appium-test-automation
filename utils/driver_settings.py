from appium import webdriver
from appium.options.common import AppiumOptions
from utils.android_utils import android_get_desired_capabilities


def create_driver():
    capabilities = android_get_desired_capabilities()

    appium_server_url = 'http://127.0.0.1:4723'

    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
    return driver
