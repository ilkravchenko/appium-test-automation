from logger.log import Logging
import pytest
from tests.login.conftest import user_login_fixture


@pytest.mark.parametrize("credentials, expected_results, option_text, expected_results_menu", [
    ("valid", True, "settings", True),  # App Settings test
    ("valid", True, "settings", False),  # False App Settings test
    ("valid", True, "help", True),  # Help test
    ("valid", True, "logs", True),  # Report a Problem test
    ("valid", True, "camera", True),  # Video Surveillance test
    ("valid", True, "addHub", True),  # Add Hub test
    ("valid", True, "documentation_text", True),  # Terms of Service test
], indirect=True)
def test_main_menu_via_nested_element(menu_option_fixture, user_login_fixture, credentials, expected_results,
                                      option_text,
                                      expected_results_menu):
    logger = Logging()

    login_page = user_login_fixture
    main_menu_page = menu_option_fixture
    login_page.credentials = credentials  # Update credentials in the LoginPage instance

    login_page.login_page_automation()

    logger.logging_info(f"Starting nested menu test for option: {option_text}\n")
    main_menu_page.nested_menu_option("ID", "com.ajaxsystems:id/menuDrawer",
                                      'ID', option_text)

    menu_success = main_menu_page.check_menu_success(option_text)
    assert menu_success == expected_results_menu
    logger.logging_info(f"Nested menu option test passed for credentials: {option_text}")

    logger.logging_info("Nested menu option test completed.\n\n\n")
