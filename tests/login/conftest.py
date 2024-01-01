import pytest
from framework.login_page import LoginPage
from utils.android_utils import android_get_valid_credentials, android_get_invalid_credentials
from utils.driver_settings import create_driver


@pytest.fixture(scope='function')
def driver():
    # Assuming you have a driver creation function, create the driver here
    driver = create_driver()
    yield driver


@pytest.fixture(scope='function')
def credentials(request):
    # Define your credentials fixture logic here
    valid_credentials = android_get_valid_credentials()
    invalid_credentials = android_get_invalid_credentials()

    if request.param == "valid":
        return valid_credentials
    elif request.param == "invalid":
        return invalid_credentials
    else:
        raise ValueError("Invalid credentials type specified")


@pytest.fixture(scope='function')
def expected_results(request):
    return request.param


@pytest.fixture(scope='function')
def user_login_fixture(driver, credentials, expected_results):
    yield LoginPage(driver, credentials)
