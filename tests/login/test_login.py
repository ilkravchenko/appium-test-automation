from logger.log import Logging
from utils.android_utils import *
import pytest

valid_credentials = android_get_valid_credentials()
invalid_credentials = android_get_invalid_credentials()
capabilities = android_get_desired_capabilities()


@pytest.mark.parametrize("credentials, expected_results", [
    ("valid", True),  # Positive test case
    ("invalid", True)  # Negative test case
], indirect=True)
def test_user_login(user_login_fixture, credentials, expected_results):
    logger = Logging()
    logger.logging_info(f"Starting login test for credentials: {credentials}\n")

    login_page = user_login_fixture
    login_page.credentials = credentials  # Update credentials in the LoginPage instance

    login_page.login_page_automation()

    login_successful = login_page.check_login_success()
    assert login_successful == expected_results, f"Login test passed for credentials: {credentials}"
    logger.logging_info("Login test completed.\n\n\n")
