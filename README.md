### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд). - **(dir framework/page)**
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы). - **(dir framework/login_page)**
3) Использовать параметризацию. - **(dir tests/login)**
4) Закомитить выполненное задание на гитхаб.

### Дополнительное задание (опционально)
1) *Реализовать логирование теста. - **(dir logger/log)**
2) *Реализовать динамическое определение udid телефона через subprocess - **(dir utils/dynamic_udid)**
3) **Написать на проверку элементов SideBar (выезжающее меню слева). - **(dir framework/main_menu)  (dir tests/main_menu/)**

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - https://appium.io/docs/en/2.0/quickstart/
5) Инспектор приложения - https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/



## Project Structure
```
Appium-automation/
    ┣ framework/ - framework for automation
        ┣ page - Main class for basic work with apps
        ┣ login_page - Class for working with login page
        ┣ main_menu - Class for working with Sidebar
    ┣ logger/ - Class for logging
    ┣ logs/ - Folder for saving log files
    ┣ tests/ - Folder for tests
        ┣ login/ - tests for login positive and negative cases
        ┣ main_menu/ - tests for menu options
            ┣ test_main_menu/ - tests for menu options 7 cases - 1 negarive 6 positive
            ┣ test_nested_main_menu/ - tests for menu options via nested element 7 cases - 1 negarive 6 positive
    ┣ utils/ - folder for utils
        ┣ android_utils - android utils for credentails and capabilities
        ┣ driver_settings - utils for driver settings
        ┣ dynamic_udid - util for get names of udid
    ┣ .gitignore
    ┣ main.py 
    ┣ pytest.ini
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/ilkravchenko/appium-test-automation.git
```


Install dependencies

```bash
  pip install -r requirements.txt
```



## Running Tests

To run tests, run the following command

```bash
  pytest
```

Tests directory:

```bash
  tests\
```

Using this command you can run 116 project's test and can see that these all tests were passed excluding 2 because this cases should not passed. All created tests are listed below:
* **login\test_login** - 2 tests for loging - negative and positive tests
  * positive case - valid credentails
  * negative case - invalid credentails
* **main_menu\test_main_menu** - 7 tests for main_menu options - 1 False case and 6 Pass cases
  * False case - invalid result for App Settings Sidebar option
  * Pass case - valid result for App Settings Sidebar option
  * Pass case - valid result for Help Sidebar option
  * Pass case - valid result for Report a Problem Sidebar option
  * Pass case - valid result for Video Surveillance Sidebar option
  * Pass case - valid result for Add Hub Sidebar option
  * Pass case - valid result for Terms of Service Sidebar option
* **main_menu\test_main_menu_via_nested_element** - 7 tests for main_menu options - 1 False case and 6 Pass cases
  * False case - invalid result for App Settings Sidebar option
  * Pass case - valid result for App Settings Sidebar option
  * Pass case - valid result for Help Sidebar option
  * Pass case - valid result for Report a Problem Sidebar option
  * Pass case - valid result for Video Surveillance Sidebar option
  * Pass case - valid result for Add Hub Sidebar option
  * Pass case - valid result for Terms of Service Sidebar option


```bash
============================== test session starts =======================================
platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\Админ\Desktop\dev_in_test_app_team
configfile: pytest.ini
collected 16 items

tests\login\test_login.py ..       [ 12%]
tests\main_menu\test_main_menu.py .F.....          [ 56%]
tests\main_menu\test_nested_main_menu.py .F....  .           [ 100%]                                                       
========================= short test summary info ===================================== 
FAILED tests/main_menu/test_main_menu.py::test_main_menu[valid-True-settings-False] - assert True == False
FAILED tests/main_menu/test_nested_main_menu.py::test_main_menu_via_nested_element[valid-True-settings-False] - assert True == False
=================== 2 failed, 14 passed in 1087.43s (0:18:07) =======================

```
