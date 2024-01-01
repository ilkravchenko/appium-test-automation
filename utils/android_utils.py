def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 200,
        'noSign': True,
        'platformName': 'Android',
        'resetKeyboard': True,
        'unicodeKeyboard': True,
        'takesScreenshot': True,
        'udid': '11c9ed357d27',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


def android_get_valid_credentials():
    return {
        'email': 'qa.ajax.app.automation@gmail.com',
        'password': 'qa_automation_password'
    }


def android_get_invalid_credentials():
    return {
        'email': 'invalid_email@example.com',
        'password': 'invalid_password'
    }
