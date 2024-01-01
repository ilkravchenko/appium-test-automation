import time
from .page import Page
from utils.android_utils import android_get_valid_credentials, android_get_invalid_credentials

valid_credentials = android_get_valid_credentials()
invalid_credentials = android_get_invalid_credentials()


class LoginPage(Page):

    def __init__(self, driver, credentials):
        super().__init__(driver)
        self.credentials = credentials

    def login_page_automation(self):
        start_page_login_btn = self.find_element(strategy="XPATH",
                                                 selector='//*[@text="Log In"]')
        self.click_element(start_page_login_btn)

        email = self.find_element(strategy="XPATH",
                                  selector='(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')
        self.input_keys(email, value=self.credentials['email'])

        password = self.find_element(strategy="XPATH",
                                     selector='(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]')
        self.input_keys(password, value=self.credentials['password'])

        submit_login_btn = self.find_element(strategy="XPATH",
                                             selector='//*[@text="Log In"]')
        self.click_element(submit_login_btn)

        time.sleep(10)

    def check_login_success(self):
        if self.credentials == android_get_valid_credentials():
            success_message = self.find_element("ID", 'com.ajaxsystems:id/hubAdd')
            result = True if success_message is not None else False

            return result
        else:
            error_message = self.find_element("XPATH", '//*[@text="Log In"]')
            result = True if error_message is not None else False

            return result
