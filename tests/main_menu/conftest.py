import pytest
from framework.main_menu import Menu
from utils.driver_settings import create_driver
from tests.login.conftest import credentials, expected_results


@pytest.fixture(scope='function')
def driver():
    # Assuming you have a driver creation function, create the driver here
    driver = create_driver()
    yield driver


@pytest.fixture(scope='function')
def option_text(request):
    return request.param


@pytest.fixture(scope='function')
def expected_results_menu(request):
    return request.param


@pytest.fixture(scope='function')
def menu_option_fixture(driver, credentials, expected_results, option_text, expected_results_menu):
    yield Menu(driver, option_text)
