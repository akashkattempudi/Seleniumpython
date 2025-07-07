import pytest
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
@pytest.fixture()
def sample():
    options = Options()  # Run Edge in headless mode
    a = webdriver.Edge()
    a.implicitly_wait(5)
    yield a
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # only take screenshot if test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("sample")
        print("Driver in report:", driver)# sample is your fixture name
        if driver:
            # generate a unique screenshot filename
            time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshot_{time_stamp}.png"
            screenshot_path = os.path.join(os.getcwd(), screenshot_name)
            driver.save_screenshot(screenshot_path)

            # attach to html report
            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(screenshot_path))
            else:
                report.extra = [pytest_html.extras.image(screenshot_path)]

# Register plugin
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
