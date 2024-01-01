from framework.page import Page

menu_options_results = {
    "settings": ["com.ajaxsystems:id/toolbarTitle", 'Settings'],  # App Settings test
    "help": ["com.ajaxsystems:id/toolbarTitle", 'Installation Manuals'],  # Help test
    "logs": ["com.ajaxsystems:id/title", 'Report a Problem'],  # Report a Problem test
    "camera": ["com.ajaxsystems:id/toolbarTitle", 'Video Surveillance'],  # Video Surveillance test
    "addHub": ["com.ajaxsystems:id/toolbarTitle", 'Add Hub'],  # Add Hub test
    "documentation_text": ["com.ajaxsystems:id/toolbarTitle", 'Terms of Service'],  # Terms of Service test
}


class Menu(Page):

    def __init__(self, driver, credentials):
        super().__init__(driver)
        self.credentials = credentials
        self.menu_options_results = menu_options_results

    def menu_automation(self, menu_strategy: str, menu_id: str, list_option_strategy: str, list_option_selector: str):
        self.select_from_menu(menu_strategy=menu_strategy, menu_id=menu_id,
                              list_option_strategy=list_option_strategy, list_option_selector=list_option_selector)

    def nested_menu_option(self, strategy, selector, nested_strategy, nested_selector):
        self.find_nested_element(strategy, selector,
                                 nested_strategy, nested_selector)

    def check_menu_success(self, option):
        if option == 'logs':
            element_for_option = self.find_element("ID", self.menu_options_results[option][0])
            result = True if element_for_option.text == self.menu_options_results[option][1] else False
            return result
        else:
            element_for_option = self.find_element("ID", self.menu_options_results[option][0])
            result = True if element_for_option.text == self.menu_options_results[option][1] else False
            return result
