from framework.login_page import LoginPage
from framework.main_menu import Menu
from utils.android_utils import android_get_desired_capabilities, android_get_invalid_credentials, \
    android_get_valid_credentials
from appium import webdriver
from appium.options.common import AppiumOptions

capabilities = android_get_desired_capabilities()

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))

login = LoginPage(driver, credentials=android_get_valid_credentials())
menu = Menu(driver, credentials=android_get_valid_credentials())
login.login_page_automation()
